HL:	MOV R0,#22		; 1 cs
	MOV R1,#1		; 1 cs
	CALL WAIT		; 2 cs
	JUMP HL


        MOV R2,#2
T0:	CALL N0
        DJNZ R2, T0


N0:	MOV R1,#1
	MOV R0,#1
	SETB P0.7
	CALL WAIT
	MOV R1,#1
	MOV R0,#1
	CALL WAIT
	CLR P0.7
	RET





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

W119:	MOV R0,#63	; 1 cs
W119R0:	DJNZ R0,W119R0	; R0 * 2 cs

W40:	MOV R1,#15	; 1 cs
W40R1:	MOV R0,#15	; R1 * 1 cs
W40R0:	DJNZ R0,W40	; R0 * 2 cs
	DJNZ R1,W40R1	; R1 * 2 cs

	RET		; 2 cs
			; nad 40
			; celkem (120 - n) + R0 * 2
			; pod 40
			; celkem 80 + R0 * 2 + (41 - n) * (1 + R0 * 2 + R1 * 3)



W12:	MOV R0,#3	; 1 cs
W12R0:	NOP		; 1 cs 
	DJNZ R0,W12R0	; R0 * (2 + n of NOP) cs



W31:	MOV R1,#7	; 1 cs
W31R1:	MOV R0,#7	; 1 cs
W31R0:	DJNZ R0,W31R0	; R0 * 2 cs
	DJNZ R1,W31R1	; R1 * 2 cs

	RET		