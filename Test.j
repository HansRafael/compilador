.source Test.src
.class  public Test
.super  java/lang/Object

.method public <init>()V
    aload_0
    invokenonvirtual java/lang/Object/<init>()V
    return
.end method

.method public static main([Ljava/lang/String;)V

    ldc 1
    istore 0
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc 2
    invokestatic Runtime/readInt()I
    iload 0
    ldc 3
    imul
    iadd
    iadd
    invokevirtual java/io/PrintStream/println(I)V

    return
.limit stack 10
.limit locals 1
.end method

; symbol_table: ['y']

; usedVars: [True]
