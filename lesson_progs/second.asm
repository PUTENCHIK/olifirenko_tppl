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
	mov rcx, 10
	xor rdx, rdx	
	; mov rdx, 0
	mov rax, 123
	div rcx 		; rdx - reminder, rax - quotent
	add rdx, '0'
	mov [result], rdx
	print result, 1
	print newline, nlen
	

	print done, len
	print newline, nlen
	mov rax, 60
	xor rdi, rdi
	syscall

section .data
	done db 'Done'
	len equ $ - done
	newline db 0xA, 0xD
	nlen equ $ - newline

section .bss
	result resb 1
	
