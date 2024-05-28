var ws,
  LastNav = null,
  Timer = null;
var keyRepeatTimer = null;

$(document).ready(function () {
  if ("WebSocket" in window) {
    var Host = window.location.hostname;
    ws = new WebSocket("ws://" + Host + ":8214", "Lux_WS");
    ws.onopen = function () {
      password_prompt(function (PW) {
        if (!PW.length) PW = "0";
        ws.send("LOGIN;" + PW);
        Timer = setInterval(requestPageRefresh, 1000);
      });
    };

    ws.onmessage = function (evt) {
      processResponse($.parseXML(evt.data));
    };

    ws.onclose = function (evt) {
      alert("Lost connection to controller!");
      if (Timer) clearInterval(Timer);
      clearKeyRepeat();
      ws = null;
    };
  } else alert("WebSocket NOT supported by your Browser!");
});

function requestPageRefresh() {
  if (ws) ws.send("REFRESH");
}

function BuildChildren(element, Container, ItemFunc) {
  var El = $(element),
    Children = El.children("item"), //Fetches only the direct children of the node.
    BaseID = El.attr("id"),
    Item = {
      ID: BaseID,
      options: new Array(),
      Depth: 0,
      hasChildren: Children.length > 0,
      Container: Container,
      ChildFunc: ItemFunc,
    },
    Diver = Children,
    Values = new Array();

  while (Diver.length > 0) {
    Diver = Diver.children("item");
    Item.Depth += 1;
  }

  El.children(":not(item)").each(function () {
    var Value = $(this).text();
    var name = this.nodeName;

    if (name == "option")
      Item["options"].push({ Text: Value, Val: $(this).attr("value") });
    else if (name == "value") Values.push(Value);
    else if (name == "columns" || name == "headers") {
      if (Item[name] == undefined) Item[name] = new Array();
      Item[name].push(Value);
    } else Item[name] = Value;
  });

  if (Values.length > 1) {
    var BaseName = Item.name,
      Index = 0;
    while (true) {
      Item.value = Values[Index];
      Item.name = BaseName + " " + ++Index;
      if (Index == Values.length) break;
      Container.append(ItemFunc(Item));
      Item.ID = BaseID + "_" + Index;
    }
  } else if (Values.length > 0) Item.value = Values[0];

  if (Children.length == 1 && Children[0].lastChild.nodeName == "img")
    buildRemoteDisplay(Container, Children[0]);
  else {
    Container.append(ItemFunc(Item));
    Children.each(function () {
      BuildChildren(this, Item.Container, Item.ChildFunc);
    });
  }
}

//------------------------------------------------------------------------
function processResponse(xmlDoc) {
  var XML = $(xmlDoc);
  var OpNode = XML.find(":root"),
    Cont_ID = OpNode.prop("tagName");

  if (Cont_ID.toUpperCase() == "VALUES") {
    XML.find("item").each(function () {
      var field = $(this),
        BaseID = field.attr("id"),
        Values = field.children("value");
      refreshMultipleLines(BaseID, Values);
    });
  } else {
    var Container = $("#" + Cont_ID),
      ItemFunc;

    Container.empty();
    $("#submitBox").remove();

    if (Cont_ID == "Navigation") {
      ItemFunc = function (Item) {
        var Line = null;
        if (hasNotEmptyProperty(Item, "name")) Line = buildNavLine(Item);
        else if (Item.hasChildren)
          Item.Container = Line = $("<ul class='nav'>");
        return Line;
      };
    } else {
      var hasSettings = XML.find("raw").length > 0;
      ItemFunc = function (Item) {
        var Line;
        Item.hasSettings = hasSettings;
        if (Item.hasChildren) {
          if (Item.Depth == 1) {
            var table = $("<table>");
            var row = $("<tr>");
            Line = $("<div>");

            if (Item.hasOwnProperty("headers")) {
              var count = Item.headers.length;
              table.append(
                "<tr><th colspan=" + count + ">" + Item.name + "</th></tr>"
              );

              for (var i = 0; i < count; ++i)
                row.append("<th>" + Item.headers[i] + "</th>");
            } else row.append("<th colspan=3>" + Item.name + "</th>");

            table.append(row);
            Item.Container = table.appendTo(Line);
          } else Line = Item.Container = $("<div>");
        } else Line = buildLine(Item);

        return Line;
      };

      if (hasSettings) buildSubmitBox();
    }
    BuildChildren(OpNode, Container, ItemFunc, 0);
    $("#EVO_overlay_container").hide();
  }
}

function refreshMultipleLines(BaseID, Values) {
  var ID = BaseID,
    i = 0;
  while (i < Values.length) {
    refreshLine(ID, document.getElementById(ID), Values[i].textContent);
    ID = BaseID + "_" + ++i;
  }
}

function refreshLine(ID, Item, Value) {
  if (Item) {
    if (Item.nodeName == "CANVAS") drawControl(Item, Value);
    else if (Value.length > 0) {
      var Set = document.getElementById("set_" + ID);
      Item.innerHTML = Value;
      if (Set && Set.nodeName == "TD") Set.innerHTML = Value;
    }
  }
}

function buildLine(Item) {
  var Line = $("<tr>");

  if (Item.hasOwnProperty("columns")) {
    for (var i = 0; i < Item.columns.length; ++i)
      Line.append("<td>" + Item.columns[i] + "</td>");
  } else {
    var NameCol = $('<td class="output_field_long">' + Item.name + "</td>");

    Line.append(NameCol);
    if (hasNotEmptyProperty(Item, "value")) buildValueLine(Line, Item);
    else NameCol.attr("colspan", "3");
  }

  return Line;
}

function hasNotEmptyProperty(Item, PropertyName) {
  return Item.hasOwnProperty(PropertyName) && Item[PropertyName].length > 0;
}

function buildNavLine(Item) {
  var Line = $("<li />");
  var Link = $("<a>" + Item.name + "</a>");
  var onClick = null;

  Line.append(Link);

  if (!Item.hasOwnProperty("readOnly") || !Item.readOnly) {
    onClick = function () {
      if ($(this) != LastNav) {
        $("#EVO_overlay_container").show();
        LastNav = $(this);
        $(".hover").removeClass("hover");
        ws.send("GET;" + Item.ID);
      }

      return false;
    };

    Link.click(onClick);
  }

  if (Item.hasChildren) {
    var Container = $("<ul>");
    Item.Container.append(Line);
    Line.append(Container);
    Item.Container = Container;

    Link.on("touchstart", function (e) {
      if (onClick && $(this).parent().hasClass("hover")) onClick();
      else {
        $(".hover").removeClass("hover");
        Link.parentsUntil("nav").addClass("hover");
      }
      e.preventDefault();
      return false;
    });
  }
  return Line;
}

function buildRemoteDisplay(container, item) {
  var ctrlDiv = $("<div id='RemoteDisplay' tabindex='-1'>");
  var overlay = $("<span id='Overlay'>");
  var canvas = createCanvas($(item).attr("id"));
  var ctrlPanel = $("<span id='CtrlPanel'>");
  var createButton = function (direction, img) {
    var item = $('<input type="image" src="' + img + '.png">');

    if (direction == 2) {
      item.mousedown(function (e) {
        sendMove(2);
        e.preventDefault();
      });
      item.mouseup(function (e) {
        sendMove(6);
        e.preventDefault();
      });
    } else {
      img = item[0];
      img.moveFunc = function () {
        sendMove(direction);
      };
      item.mousedown(function (e) {
        sendMove(direction, 2);
        e.preventDefault();
      });

      item.mouseup(clearKeyRepeat);
    }

    return item;
  };

  overlay.append("<img src='LuxSim.jpg'>");
  overlay.append(canvas);

  ctrlPanel.append(createButton(1, "Up"));
  ctrlPanel.append(createButton(2, "OK"));
  ctrlPanel.append(createButton(0, "Down"));

  ctrlDiv.append(overlay);
  ctrlDiv.append(ctrlPanel);
  container.append(ctrlDiv);
  registerListenersToRemoteControl(ctrlDiv, overlay);
}

function createCanvas(ID) {
  var Canvas = document.createElement("canvas");
  (Ctx = Canvas.getContext("2d")), (Ctx.canvas.width = 320);
  Ctx.canvas.height = 160;
  Canvas.id = ID;
  return Canvas;
}

function registerListenersToRemoteControl(ControlDiv, mouseArea) {
  var sendMouseDown = function (e) {
      sendMove(2);
      e.preventDefault();
    },
    sendMouseUp = function (e) {
      sendMove(6);
      e.preventDefault();
    };

  mouseArea.mousedown(sendMouseDown);
  mouseArea.mouseup(sendMouseUp);

  ControlDiv.keydown(function (evt) {
    switch (evt.keyCode) {
      case 37:
      case 38:
        sendMove(1);
        break;
      case 39:
      case 40:
        sendMove(0);
        break;
      case 32:
      case 13:
        sendMove(2);
        break;
    }
    evt.preventDefault();
  });

  ControlDiv.keyup(sendMouseUp);

  ControlDiv.bind("mousewheel DOMMouseScroll", function (e) {
    var evt = e.originalEvent,
      delta = evt.wheelDelta == undefined ? evt.detail * -1 : evt.wheelDelta,
      direction = delta > 0 ? 1 : 0;

    sendMove(direction);
    e.preventDefault();
  });
  ControlDiv.focus();
}

//0 - Repeat, 1 - Clear and do not repeat, 2 - Clear and do repeat
function sendMove(direction, enableKeyRepeat = 1) {
  if (ws) {
    if (enableKeyRepeat > 0) {
      clearKeyRepeat();
      if (enableKeyRepeat == 2)
        keyRepeatTimer = setInterval(function () {
          sendMove(direction, 0);
        }, 250);
    }
    ws.send("MOVE;" + direction);
  }
}

function clearKeyRepeat() {
  if (keyRepeatTimer) {
    clearInterval(keyRepeatTimer);
    keyRepeatTimer = null;
  }
}

function drawControl(To, Code) {
  var Src = atob(Code),
    Canvas = document.createElement("canvas"),
    Ctx = Canvas.getContext("2d"),
    Image = Ctx.createImageData(160, 64),
    Data = Image.data;
  for (var Row = 0, o = 0; Row < 8; ++Row) {
    for (var Col = 0; Col < 160; ++Col, ++o) {
      var Index = Row * 5120 + Col * 4,
        Byte = Src[o].charCodeAt();
      for (var i = 0; i < 8; ++i) {
        var color = Byte & (1 << i) ? 0xff : 0x00;
        Data[Index + 0] = color; //R
        Data[Index + 1] = color; //G
        Data[Index + 2] = 0xff; //B
        Data[Index + 3] = 255; //Alpha
        Index += 640; //Pixel below the one we just had.
      }
    }
  }
  Ctx.putImageData(Image, 0, 0); //Okay, done with drawing.

  To.getContext("2d").drawImage(
    Canvas,
    0,
    0,
    160,
    64, //From position
    0,
    0,
    320,
    128 //To position
  );
  return To;
}

function buildValueLine(Line, Item) {
  var ValCol = $(
      "<td id=" + Item.ID + ' class="output_field">' + Item.value + "</td>"
    ),
    NewEl = null;
  Line.append(ValCol);
  if (Item.hasOwnProperty("raw")) NewEl = buildSettingLine(Item);
  else if (Item.hasOwnProperty("multiple"))
    NewEl = buildTooltip(ValCol, filterOptions(Item));
  else if (Item.hasOwnProperty("list"))
    NewEl = buildTooltip(ValCol, Item.options);

  if (NewEl) {
    var SettingColumn = $('<td class="output_field">');
    var parents = NewEl.parents();
    NewEl.val(Item.raw);
    NewEl.change(function () {
      if (ws) {
        var El = $(this);
        var value = El.val();
        var div = El.data("Div");
        if (div != undefined) value *= div;
        ws.send("SET;" + El.attr("id") + ";" + value);
      }
    });
    if (parents.length > 0) NewEl = parents[0];
    Line.append(SettingColumn.append(NewEl));
  } else if (Item.hasSettings)
    Line.append(ValCol.clone().attr("id", "set_" + Item.ID));
  else ValCol.attr("colspan", "2");
}

function buildSettingLine(Item) {
  if (!Item.hasOwnProperty("type")) {
    if (Item.options.length)
      Item.type = Item.hasOwnProperty("multiple") ? "checklist" : "combo";
    else if (Item.hasOwnProperty("min")) Item.type = "slider";
  }

  switch (Item.type) {
    case "checklist":
      return buildCheckListSetting(Item);
    case "combo":
      return buildComboSetting(Item);
    case "combi":
      return buildCombiSetting(Item);
    case "slider":
      return buildTemperatureSetting(Item);
    case "timer":
      return buildTimerLine(Item);
  }
  return null;
}

function buildCheckListSetting(Item) {
  var Container = $('<div class="CheckList">'),
    NewEl = $('<input type="hidden" id=set_' + Item.ID + ">"),
    Options = Item.options;
  for (var i = 0; i < Options.length; ++i) {
    var Cbx = $(
      '<input type="checkbox" value="' +
        Options[i].Val +
        '">' +
        Options[i].Text +
        "</input>"
    );
    Cbx.prop("checked", (Item.raw & (1 << i)) > 0);
    Cbx.change(function () {
      var Val = NewEl.val(),
        Bit = 1 << Cbx.val();
      if (Cbx.prop("checked")) Val |= Bit;
      else Val &= ~Bit;
      NewEl.val(Val).change();
    });
    Container.append(Cbx);
  }
  return NewEl;
}

function buildComboSetting(Item) {
  var NewEl = $("<select id=set_" + Item.ID + ">"),
    Options = Item.options;

  for (var i = 0; i < Options.length; ++i)
    NewEl.append(
      '<option value="' + Options[i].Val + '">' + Options[i].Text + "</option>"
    );
  return NewEl;
}

function buildCombiSetting(item) {
  var Options = item.options;
  var max = parseInt(item.max);
  var step = parseInt(item.step);

  for (var i = parseInt(item.min); i <= max; i += step)
    Options.push({ Text: i + item.unit, Val: i });
  Options.sort((f, s) => {
    return f.Val - s.Val;
  });

  return buildComboSetting(item);
}

function buildTemperatureSetting(Item) {
  var container = $('<span class="input_span" />');
  var newEl = $(
    '<input type="number" min="' +
      Item.min / Item.div +
      '" max="' +
      Item.max / Item.div +
      '" step="' +
      Item.step / Item.div +
      '" id="set_' +
      Item.ID +
      '">'
  );
  Item.raw /= Item.div;
  newEl.data("Div", Item.div);
  container.append(newEl);
  if (Item.unit.length > 0)
    container.append('<span class="Unit">' + Item.unit + "</span>");

  return newEl;
}

function filterOptions(Item) {
  var options = Item.options;
  var value = Item.value;
  var result = [];

  for (var i = 0; i < options.length; ++i) {
    if (value & (1 << i)) result.push(options[i]);
  }

  return result;
}

function buildTooltip(Container, content) {
  var ToolTip = $('<span class="tooltip">');
  for (var i = 0; i < content.length; ++i)
    ToolTip.append(content[i].Text + "<br />");
  Container.addClass("toolbox");
  Container.append(ToolTip);
}

function buildTimerLine(item) {
  var container = $("<span />"),
    newEl = $('<input type="hidden" id=set_' + item.ID + ">"),
    timeValues = [item.raw & 0xffff, item.raw >> 16],
    separators = [":", " - ", ":", ""];

  for (var o = 0, pos = 0; o < 2; ++o) {
    var value = timeValues[o];

    for (var i = 0; i < 2; ++i, ++pos) {
      var maxTime = !i ? 23 : 59;
      var boxValue = !i ? Math.floor(value / 60) : value % 60;
      var timeBox = $(
        '<input type="number" min="0" max="' +
          maxTime +
          '" step="1" value="' +
          boxValue +
          '" />'
      );
      timeBox.data("shiftIndex", o);

      timeBox.change(function () {
        var el = $(this);
        var shiftIndex = el.data("shiftIndex");
        var value = timeValues[shiftIndex];
        var boxIndex = el.attr("max") == 23 ? 0 : 1;

        value = [Math.floor(value / 60), value % 60];
        value[boxIndex] = parseInt(el.val(), 10);
        timeValues[shiftIndex] = value[0] * 60 + value[1];
        newEl.val((timeValues[1] << 16) + timeValues[0]).change();
      });
      container.append(timeBox);
      container.append(separators[pos]);
    }
  }
  container.append(newEl);

  return newEl;
}

function buildSubmitBox() {
  var Submit = $('<img id="submitBox" src="saveIcon.png">');

  Submit.click(function () {
    if (ws) ws.send("SAVE;1");
    return false;
  });

  $("#Navigation").prepend(Submit);
}
//------------------------------------------------------------------------

function password_prompt(callback) {
  var input = $("#password_prompt_input"),
    prompt = document.getElementById("password_prompt"),
    button = $("#password_submit_button");

  var submit = function () {
    callback(input.val());
    prompt.removeAttribute("style");
    input.val("");
  };

  input.on("keydown", function (e) {
    if (e.keyCode == 13) {
      $(this).off();
      submit();
    }
  });
  button.one("click", submit);

  prompt.style.display = "block";
  input.focus();
}
