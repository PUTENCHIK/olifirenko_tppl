%macro print 2
	mov rax, 1
	mov rdi, 1
	mov rsi, %1
	mov rdx, %2
	syscall
%endmacro

section .text
global _start

_start:
	mov rax, [value]
	and rax, 1
	cmp rax, 0
	jne odd

even:
	print message2, len2
	jmp end

odd:
	print message1, len1
	jmp end

end:

section .data
	value db 16
	message1 db 'Is odd', 0xA, 0xD
	len1 equ $ - message1
	message2 db 'Is even', 0xA, 0xD
	len2 equ $ - message2
