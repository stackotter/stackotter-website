import angr
import claripy

proj = angr.Project(
    'st_angr', 
    main_opts = {'base_addr': 0x0}, 
    load_options = {'auto_load_libs': False}
)

def cast_to_c_char(x):
    return x & 0xff

def convert_bool_to_uint(x):
    return 1 if x else 0

# Flag is 10 characters
flag = claripy.BVS("flag", 8 * 60)

state = proj.factory.entry_state(stdin = flag)

# Silence the warnings
state.options.add(angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY)

state.solver.add((flag.get_byte(1) - 1) == (flag.get_byte(2) - 2) + 1)
state.solver.add((flag.get_byte(1) - 1) == flag.get_byte(0) + 0x2a)
# state.solver.add((cast_to_c_char(flag.get_byte(1) - 1) - cast_to_c_char(flag.get_byte(3) - 3) ==        (cast_to_c_char(flag.get_byte(5) - 5) - cast_to_c_char(flag.get_byte(2) - 2)) + 5))
state.solver.add(((((flag.get_byte(3) - 3) ^ (flag.get_byte(1) - 1)) == 0x37)))
state.solver.add((((flag.get_byte(6) - 6) - (flag.get_byte(7) - 7)) * -2 == (flag.get_byte(8) - 8)))
state.solver.add(((((flag.get_byte(7) - 7) - (flag.get_byte(6) - 6)) * 3 == (flag.get_byte(9) - 9) - (flag.get_byte(10) - 10))))
state.solver.add(((flag.get_byte(2) - 2) + (flag.get_byte(3) - 3) == (flag.get_byte(5) - 5) + (flag.get_byte(4) - 4) + 3))
state.solver.add(((((flag.get_byte(2) - 2) - (flag.get_byte(5) - 5)) * 2 == (flag.get_byte(6) - 6) - (flag.get_byte(7) - 7))))
state.solver.add(((flag.get_byte(3) - 3) - (flag.get_byte(7) - 7) == 1))
state.solver.add((((flag.get_byte(5) - 5) - (flag.get_byte(3) - 3) == ((flag.get_byte(4) - 4) - (flag.get_byte(6) - 6)) * 3)))
state.solver.add((((flag.get_byte(3) - 3) == 92)))
state.solver.add((((flag.get_byte(4) - 4) - (flag.get_byte(5) - 5)) * -3 == (flag.get_byte(8) - 8) + (flag.get_byte(6) - 6)))
state.solver.add((((((flag.get_byte(4) - 4) - (flag.get_byte(6) - 6)) + 0x32) * 2 == (flag.get_byte(5) - 5))))
state.solver.add((((flag.get_byte(6) - 6) & (flag.get_byte(5) - 5)) == 0x44))
state.solver.add((((flag.get_byte(5) - 5) == 0x74)))
state.solver.add((((flag.get_byte(6) - 6) - (flag.get_byte(7) - 7)) * -2 == (flag.get_byte(8) - 8)))
state.solver.add(((((flag.get_byte(7) - 7) - (flag.get_byte(6) - 6)) * 3 == (flag.get_byte(9) - 9) - (flag.get_byte(10) - 10))))
state.solver.add((((flag.get_byte(7) - 7) - (flag.get_byte(9) - 9)) * -5 == (flag.get_byte(8) - 8)))
state.solver.add(((flag.get_byte(8) - 8) * 3 == ((flag.get_byte(9) - 9) - (flag.get_byte(10) - 10)) * 2))
state.solver.add((((flag.get_byte(8) - 8) - (flag.get_byte(10) - 10) == 1)))
state.solver.add(((flag.get_byte(9) - 9) % 10 == (flag.get_byte(10) - 10) % 10))
state.solver.add((((flag.get_byte(9) - 9) % 10 == 9)))
state.solver.add((((flag.get_byte(9) - 9) * 8 == (flag.get_byte(11) - 11) * 9)))
# state.solver.add((cast_to_c_char((flag.get_byte(11) - 11) ^ (flag.get_byte(10) - 10)) != convert_bool_to_uint((flag.get_byte(12) - 12) == 0x2c)))
state.solver.add(((flag.get_byte(11) - 11) - (flag.get_byte(12) - 12) == ((flag.get_byte(13) - 13) / 10)))
state.solver.add((((flag.get_byte(11) - 11) / 10 == (flag.get_byte(11) - 11) % 10)))
# state.solver.add((cast_to_c_char((flag.get_byte(16) - 16) ^ (flag.get_byte(12) - 12) ^ (flag.get_byte(13) - 13)) == 0x38))
state.solver.add((((flag.get_byte(12) - 12) == (flag.get_byte(16) - 16))))
state.solver.add(((flag.get_byte(13) - 13) / 10 == (flag.get_byte(14) - 14) / 0x14))
state.solver.add((((flag.get_byte(13) - 13) % 10 == (flag.get_byte(14) - 14) % 10)))
state.solver.add(((flag.get_byte(14) - 14) + 2 == (flag.get_byte(15) - 15) * 3))
state.solver.add((((flag.get_byte(14) - 14) + 0xd == (flag.get_byte(16) - 16) + (flag.get_byte(15) - 15))))
state.solver.add((((flag.get_byte(14) - 14) % 10 == (flag.get_byte(15) - 15) % 10)))
state.solver.add(((flag.get_byte(15) - 15) * 2 == (flag.get_byte(16) - 16) + -0xb))
state.solver.add((((flag.get_byte(15) - 15) * 3 == ((flag.get_byte(18) - 18) % 10) + (flag.get_byte(17) - 17))))
# state.solver.add((((flag.get_byte(19) - 19) * 3 - (flag.get_byte(16) - 16) ==        cast_to_c_char(cast_to_c_char((((flag.get_byte(18) - 18) * 0x10093) & 0xffff) >> 0xb) - ((flag.get_byte(18) - 18) >> 7)))))
state.solver.add((((flag.get_byte(17) - 17) + (flag.get_byte(16) - 16) == 0xb7)))
state.solver.add(((flag.get_byte(17) - 17) - (flag.get_byte(18) - 18) == (flag.get_byte(19) - 19) - (flag.get_byte(20) - 20)))
state.solver.add(((flag.get_byte(18) - 18) % 10 == (flag.get_byte(21) - 21) / 10))
state.solver.add((((flag.get_byte(18) - 18) / 10 == (flag.get_byte(21) - 21) % 10)))
state.solver.add((((flag.get_byte(18) - 18) == (flag.get_byte(20) - 20) + (flag.get_byte(19) - 19) * 2 + 10)))
state.solver.add(((flag.get_byte(19) - 19) == (flag.get_byte(20) - 20) + 2))
state.solver.add((((flag.get_byte(19) - 19) * 3 == (flag.get_byte(21) - 21) + 1)))
# state.solver.add((((cast_to_c_char(flag.get_byte(23) - 23) + cast_to_c_char(flag.get_byte(20) - 20) * 2 + 10 ==         cast_to_c_char(flag.get_byte(22) - 22) + cast_to_c_char(flag.get_byte(21) - 21)))))
# state.solver.add(((cast_to_c_char((flag.get_byte(20) - 20) ^ (flag.get_byte(21) - 21)) / 10 == cast_to_c_char(flag.get_byte(23) - 23) % 10)))
# state.solver.add(((cast_to_c_char((flag.get_byte(20) - 20) ^ (flag.get_byte(21) - 21)) % 10 == cast_to_c_char(flag.get_byte(23) - 23) / 10)))
state.solver.add((((flag.get_byte(21) - 21) - (flag.get_byte(22) - 22)) * 6 == (flag.get_byte(23) - 23)))
state.solver.add((((flag.get_byte(21) - 21) + (flag.get_byte(22) - 22) == (flag.get_byte(24) - 24) * 2)))
state.solver.add((((flag.get_byte(22) - 22) * 2) % 100 == (flag.get_byte(26) - 26)))
state.solver.add(((((flag.get_byte(23) - 23) + (flag.get_byte(22) - 22)) - 0xa9 < 0xd)))
state.solver.add((((flag.get_byte(23) - 23) - (flag.get_byte(24) - 24)) * 3 == (flag.get_byte(26) - 26) + -1))
state.solver.add(((((flag.get_byte(23) - 23) - (flag.get_byte(24) - 24)) * 4 == (flag.get_byte(25) - 25) + 1)))
state.solver.add(((flag.get_byte(24) - 24) - (flag.get_byte(25) - 25) == (flag.get_byte(27) - 27)))
state.solver.add((((flag.get_byte(24) - 24) + 10 == ((flag.get_byte(25) - 25) - (flag.get_byte(26) - 26)) * 7)))
# state.solver.add((cast_to_c_char(flag.get_byte(26) - 26) + cast_to_c_char(flag.get_byte(25) - 25) + -1 ==        cast_to_c_char(flag.get_byte(28) - 28) + cast_to_c_char(flag.get_byte(27) - 27)))
state.solver.add(((((flag.get_byte(26) - 26) ^ (flag.get_byte(25) - 25)) == 0x15)))
state.solver.add(((flag.get_byte(26) - 26) + (flag.get_byte(30) - 30) == (flag.get_byte(29) - 29) * 2))
state.solver.add((((flag.get_byte(26) - 26) % 10 == (flag.get_byte(29) - 29) % 10)      ))
state.solver.add(((flag.get_byte(27) - 27) * 3 == (flag.get_byte(29) - 29)))
state.solver.add((((flag.get_byte(27) - 27) % 10 == (flag.get_byte(28) - 28) % 10)))
state.solver.add(((flag.get_byte(29) - 29) + (flag.get_byte(28) - 28) == 0x94))
state.solver.add((((flag.get_byte(28) - 28) - (flag.get_byte(29) - 29) == 0x10)))
state.solver.add(((flag.get_byte(29) - 29) % 10 == (flag.get_byte(30) - 30) % 10))
state.solver.add(((((flag.get_byte(29) - 29) - (flag.get_byte(30) - 30)) * -2 == (flag.get_byte(31) - 31) - (flag.get_byte(32) - 32))))
state.solver.add(((flag.get_byte(30) - 30) % 10 == (flag.get_byte(31) - 31) % 10))
state.solver.add(((((flag.get_byte(30) - 30) - (flag.get_byte(31) - 31)) * 4 == ((flag.get_byte(31) - 31) - (flag.get_byte(32) - 32)) * 3)))
state.solver.add(((flag.get_byte(32) - 32) + (flag.get_byte(31) - 31) == 0x48))
state.solver.add((((flag.get_byte(33) - 33) - (flag.get_byte(31) - 31) == ((flag.get_byte(32) - 32) % 10))))
state.solver.add(((flag.get_byte(33) - 33) + (flag.get_byte(32) - 32) == 0x4e))
state.solver.add((((flag.get_byte(32) - 32) == (flag.get_byte(36) - 36))))
state.solver.add(((flag.get_byte(34) - 34) + (flag.get_byte(33) - 33) == 0x8f))
state.solver.add((((flag.get_byte(33) - 33) - (flag.get_byte(34) - 34) == -0x13)))
state.solver.add(((flag.get_byte(36) - 36) * -5 + (flag.get_byte(34) - 34) == 1))
state.solver.add((((flag.get_byte(34) - 34) - (flag.get_byte(37) - 37) == 2)))
state.solver.add(((flag.get_byte(36) - 36) * -3 + (flag.get_byte(35) - 35) == 1))
state.solver.add((((flag.get_byte(35) - 35) % 10 == (flag.get_byte(37) - 37) % 10)))
state.solver.add((((flag.get_byte(36) - 36) * 5 - (flag.get_byte(37) - 37) == 1)))
state.solver.add((flag.get_byte(37) - 37) - (flag.get_byte(39) - 39) == ((flag.get_byte(38) - 38) % 10))
state.solver.add((((((flag.get_byte(36) - 36) * 0xd == (flag.get_byte(38) - 38) << 4)))))
state.solver.add((flag.get_byte(39) - 39) + (flag.get_byte(38) - 38) * 2 == 0x66)
state.solver.add((flag.get_byte(37) - 37) - (flag.get_byte(39) - 39) == 3)

sm = proj.factory.simulation_manager(state)

sm.explore(find = lambda s: b"Congratulations" in s.posix.dumps(1), avoid = lambda s: b"Keep going" in s.posix.dumps(1))

found_count = len(sm.found)
i = 0
while len(sm.active) != 0:
    sm.step()
    i += 1
    if i % 100 == 0:
        new_found_count = len(sm.found)
        if found_count != new_found_count:
            print("New finding")
            print(sm)
            print(sm.found)
            print(sm.found[-1].posix.dumps(0))
            found_count = new_found_count

for found in sm.found:
    print(found.posix.dumps(0))
