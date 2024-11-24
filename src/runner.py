import bfi

# Not personally a fan of leaving comments in code, however this might need some explanation! Below is brainf**k code:
program = """
,[             # Read first letter
  .            # Output current letter
  [            # Loop until the end of the input (when the letter is 0)
    >[-<]      # Clear the next cell and move back to the input cell
    ,          # Read the next letter
    .          # Output the current letter
  ]
]
"""

result = bfi.interpret(program,  input_data="Hello")