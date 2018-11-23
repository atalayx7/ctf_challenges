#!usr/bin/env/ python
'''
.intel_syntax noprefix
.bits 32
    
.global asm2

asm2:
    push    ebp
    mov     ebp,esp
    sub     esp,0x10
    mov     eax,DWORD PTR [ebp+0xc]
    mov     DWORD PTR [ebp-0x4],eax
    mov     eax,DWORD PTR [ebp+0x8]
    mov DWORD PTR [ebp-0x8],eax
    jmp     part_b
part_a: 
    add     DWORD PTR [ebp-0x4],0x1
    add DWORD PTR [ebp+0x8],0xa9
part_b: 
    cmp     DWORD PTR [ebp+0x8],0x3923
    jle     part_a
    mov     eax,DWORD PTR [ebp-0x4]
    mov esp,ebp
    pop ebp
    ret

Question: What does asm2(0x8,0x21) return?
'''
ebp_plus_0x8 = 0x8
ebp_plus_0xc = 0x21
eax = ebp_plus_0xc
ebp_minus_0x4 = eax
eax = ebp_plus_0x8
ebp_plus_0x8 = eax

while True:
    if (ebp_plus_0x8 <= 0x3923):
        # part a
        ebp_minus_0x4 += 1
        ebp_plus_0x8 += 0xa9

    else:
        eax = ebp_minus_0x4
        print hex(eax)
        break
