keys_values = [
[("U", "U2", "U'"), "R R2 R' F F2 F' D D2 D' L L2 L' B B2 B'".split()],
[("R", "R2", "R'"), "U U2 U' F F2 F' D D2 D' L L2 L' B B2 B'".split()],
[("F", "F2", "F'"), "U U2 U' R R2 R' D D2 D' L L2 L' B B2 B'".split()],
[("D", "D2", "D'"), "R R2 R' F F2 F' L L2 L' B B2 B'".split()],
[("L", "L2", "L'"), "U U2 U' F F2 F' D D2 D' B B2 B'".split()],
[("B", "B2", "B'"), "U U2 U' R R2 R' D D2 D' L L2 L'".split()]]

available_moves = {key: value for keys, value in keys_values for key in keys}
available_moves.update({None: "U U2 U' R R2 R' F F2 F' D D2 D' L L2 L' B B2 B'".split()})