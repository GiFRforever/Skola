HL:	MOV R0,#22		; 1 cs
	MOV R1,#1		; 1 cs
	CALL WAIT		; 2 cs
	JUMP HL

WAIT:	DJNZ R0,WAIT		; R0 * 2 cs
	CJNE R1,#0,WAIT1	; 2 cs
	RET			; 2 cs
				; celkem 8 cs
WAIT1:	MOV R0,#255		; 1 cs
WAIT2:	DJNZ R0,WAIT2		; R0 * 2 cs
	DJNZ R1,WAIT1		; R1 * 2 cs
	RET			; 2 cs
				; celkem 16 cs
END