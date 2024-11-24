import bfi

# Not personally a fan of leaving comments in code, however this might need some explanation! Below is brainf**k code:
program = """
,[
  .
  >[-]
]
"""

result = bfi.interpret(program,  input_data="Hello")