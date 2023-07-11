funcs = ["""
undefined8 func2(char *input)

{
  int func3_ret;
  
  puts("The Sound of Perseverance");
  if ((((int)input[1] == input[2] + 1) && ((int)input[1] == *input + 0x2a)) &&
     (func3_ret = func3(input + 1), func3_ret != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func3(byte *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((int)(char)*param_1 - (int)(char)param_1[2] ==
        ((int)(char)param_1[4] - (int)(char)param_1[1]) + 5) && ((param_1[2] ^ *param_1) == 0x37))
     && (iVar1 = func4(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func8(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((((int)*param_1 - (int)param_1[1]) * -2 == (int)param_1[2]) &&
      (((int)param_1[1] - (int)*param_1) * 3 == (int)param_1[3] - (int)param_1[4])) &&
     (iVar1 = func9(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func4(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((int)*param_1 + (int)param_1[1] == (int)param_1[3] + (int)param_1[2] + 3) &&
      (((int)*param_1 - (int)param_1[3]) * 2 == (int)param_1[4] - (int)param_1[5])) &&
     (iVar1 = func5(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func5(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((((int)*param_1 - (int)param_1[4] == 1) &&
       ((int)param_1[2] - (int)*param_1 == ((int)param_1[1] - (int)param_1[3]) * 3)) &&
      (*param_1 == '\\')) && (iVar1 = func6(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func6(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((((int)*param_1 - (int)param_1[1]) * -3 == (int)param_1[4] + (int)param_1[2]) &&
      ((((int)*param_1 - (int)param_1[2]) + 0x32) * 2 == (int)param_1[1])) &&
     (iVar1 = func7(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func7(byte *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((param_1[1] & *param_1) == 0x44) && (*param_1 == 0x74)) &&
     (iVar1 = func8(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func8(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((((int)*param_1 - (int)param_1[1]) * -2 == (int)param_1[2]) &&
      (((int)param_1[1] - (int)*param_1) * 3 == (int)param_1[3] - (int)param_1[4])) &&
     (iVar1 = func9(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func9(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((int)*param_1 - (int)param_1[2]) * -5 == (int)param_1[1]) &&
     (iVar1 = func10(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func10(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((*param_1 * 3 == ((int)param_1[1] - (int)param_1[2]) * 2) &&
      ((int)*param_1 - (int)param_1[2] == 1)) && (iVar1 = func11(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func11(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((*param_1 % '\n' == param_1[1] % '\n') && (*param_1 % '\n' == '\t')) &&
      (*param_1 * 8 == param_1[2] * 9)) && (iVar1 = func12(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func12(byte *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((int)(char)(param_1[1] ^ *param_1) != (uint)(param_1[2] == 0x2c)) &&
     (iVar1 = func13(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func13(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((int)*param_1 - (int)param_1[1] == (int)(param_1[2] / '\n')) &&
      (*param_1 / '\n' == *param_1 % '\n')) && (iVar1 = func14(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func14(byte *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((byte)(param_1[4] ^ *param_1 ^ param_1[1]) == 0x38) && (*param_1 == param_1[4])) &&
     (iVar1 = func15(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func15(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((*param_1 / '\n' == param_1[1] / '\\x14') && (*param_1 % '\n' == param_1[1] % '\n')) &&
     (iVar1 = func16(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func16(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((*param_1 + 2 == param_1[1] * 3) && (*param_1 + 0xd == (int)param_1[2] + (int)param_1[1]))
      && (*param_1 % '\n' == param_1[1] % '\n')) && (iVar1 = func17(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func17(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((*param_1 * 2 == param_1[1] + -0xb) &&
      (*param_1 * 3 == (int)(param_1[3] % '\n') + (int)param_1[2])) &&
     (iVar1 = func18(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func18(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((param_1[3] * 3 - (int)*param_1 ==
        (int)(char)((char)((short)(param_1[2] * 0x10093) >> 0xb) - (param_1[2] >> 7))) &&
      ((int)param_1[1] + (int)*param_1 == 0xb7)) && (iVar1 = func19(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func19(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((int)*param_1 - (int)param_1[1] == (int)param_1[2] - (int)param_1[3]) &&
     (iVar1 = func20(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func20(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((*param_1 % '\n' == param_1[3] / '\n') && (*param_1 / '\n' == param_1[3] % '\n')) &&
      ((int)*param_1 == (int)param_1[2] + param_1[1] * 2 + 10)) &&
     (iVar1 = func21(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func21(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((int)*param_1 == param_1[1] + 2) && (*param_1 * 3 == param_1[2] + 1)) &&
     (iVar1 = func22(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func22(byte *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((((int)(char)param_1[3] + (char)*param_1 * 2 + 10 ==
         (int)(char)param_1[2] + (int)(char)param_1[1]) &&
       ((char)(*param_1 ^ param_1[1]) / '\n' == (char)param_1[3] % '\n')) &&
      ((char)(*param_1 ^ param_1[1]) % '\n' == (char)param_1[3] / '\n')) &&
     (iVar1 = func23(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func23(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((((int)*param_1 - (int)param_1[1]) * 6 == (int)param_1[2]) &&
      ((int)*param_1 + (int)param_1[1] == param_1[3] * 2)) &&
     (iVar1 = func24(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func24(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((*param_1 * 2) % 100 == (int)param_1[4]) &&
      (((int)param_1[1] + (int)*param_1) - 0xa9U < 0xd)) &&
     (iVar1 = func25(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func25(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((((int)*param_1 - (int)param_1[1]) * 3 == param_1[3] + -1) &&
      (((int)*param_1 - (int)param_1[1]) * 4 == param_1[2] + 1)) &&
     (iVar1 = func26(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func26(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((int)*param_1 - (int)param_1[1] == (int)param_1[3]) &&
      (*param_1 + 10 == ((int)param_1[1] - (int)param_1[2]) * 7)) &&
     (iVar1 = func27(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func27(byte *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((int)(char)param_1[1] + (int)(char)*param_1 + -1 ==
        (int)(char)param_1[3] + (int)(char)param_1[2]) && ((param_1[1] ^ *param_1) == 0x15)) &&
     (iVar1 = func28(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func28(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((int)*param_1 + (int)param_1[4] == param_1[3] * 2) && (*param_1 % '\n' == param_1[3] % '\n')
      ) && (iVar1 = func29(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func29(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((*param_1 * 3 == (int)param_1[2]) && (*param_1 % '\n' == param_1[1] % '\n')) &&
     (iVar1 = func30(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func30(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((int)param_1[1] + (int)*param_1 == 0x94) && ((int)*param_1 - (int)param_1[1] == 0x10)) &&
     (iVar1 = func31(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func31(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((*param_1 % '\n' == param_1[1] % '\n') &&
      (((int)*param_1 - (int)param_1[1]) * -2 == (int)param_1[2] - (int)param_1[3])) &&
     (iVar1 = func32(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func32(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((*param_1 % '\n' == param_1[1] % '\n') &&
      (((int)*param_1 - (int)param_1[1]) * 4 == ((int)param_1[1] - (int)param_1[2]) * 3)) &&
     (iVar1 = func33(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func33(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((int)param_1[1] + (int)*param_1 == 0x48) &&
      ((int)param_1[2] - (int)*param_1 == (int)(param_1[1] % '\n'))) &&
     (iVar1 = func34(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func34(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((int)param_1[1] + (int)*param_1 == 0x4e) && (*param_1 == param_1[4])) &&
     (iVar1 = func35(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func35(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if ((((int)param_1[1] + (int)*param_1 == 0x8f) && ((int)*param_1 - (int)param_1[1] == -0x13)) &&
     (iVar1 = func36(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func36(char *param_1)

{
  int iVar1;
  
  puts("The Sound of Perseverance");
  if (((param_1[2] * -5 + (int)*param_1 == 1) && ((int)*param_1 - (int)param_1[3] == 2)) &&
     (iVar1 = func37(param_1 + 1), iVar1 != 0)) {
    return 1;
  }
  return 0;
}
""",
"""
undefined8 func37(char *param_1)

{
  puts("The Sound of Perseverance");
  if (((((param_1[1] * -3 + (int)*param_1 == 1) && (*param_1 % '\n' == param_1[2] % '\n')) &&
       (param_1[1] * 5 - (int)param_1[2] == 1)) &&
      (((int)param_1[2] - (int)param_1[4] == (int)(param_1[3] % '\n') &&
       (param_1[1] * 0xd == (int)param_1[3] << 4)))) &&
     (((int)param_1[4] + param_1[3] * 2 == 0x66 &&
      (((int)param_1[2] - (int)param_1[4] == 3 && (param_1[3] * -6 + (int)param_1[4] == -2)))))) {
    return 1;
  }
  return 0;
}
"""]

for func in funcs:
    name = func.split(" ")[1].split("(")[0]
    n = int(name[4:])
    offset = n - 2
    cond_expr = func.split("if (")[1].split(") {")[0]
    conds = cond_expr.split("&&")[:-1]
    if len(conds) != 1:
        conds[0] = conds[0][1:]
        conds[-1] = conds[-1][:-1]
    for cond in conds:
        cond = cond.replace("(int)", "")
        cond = cond.replace("*param_1", "(flag[0]")
        cond = cond.replace("param_1", "(flag")
        cond = cond.replace("(char)", "cast_to_c_char")
        out = ""
        in_index = False
        index_chars = ""
        for c in cond:
            if in_index:
                if c == "]":
                    new_index = str(int(index_chars) + offset)
                    out += new_index
                    out += ")"
                    out += f" - {new_index}"
                    out += ")"
                    in_index = False
                else:
                    index_chars += c
            else:
                if c == "[":
                    index_chars = ""
                    in_index = True
                    out += ".get_byte("
                else:
                    out += c
        cond = out
        cond = cond.strip()
        cond = cond.replace("'\n'", "10")
        cond = cond.replace("'\t'", "9")
        cond = cond.replace("'\\'", "92")
        cond = cond.replace("\n", "")
        print(f"state.solver.add({cond})")
