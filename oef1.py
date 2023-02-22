import wiringpi as wp

# set up pins
IN1 = 0
IN2 = 1
IN3 = 2
IN4 = 3

# set pin modes
wiringpi.wiringPiSetup()
wiringpi.pinMode(IN1, wiringpi.OUTPUT)
wiringpi.pinMode(IN2, wiringpi.OUTPUT)
wiringpi.pinMode(IN3, wiringpi.OUTPUT)
wiringpi.pinMode(IN4, wiringpi.OUTPUT)

# define step sequence
step_sequence = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

# set initial values
step_count = len(step_sequence)
current_step = 0

# rotate motor
while True:
    for pin in range(4):
        value = step_sequence[current_step][pin]
        wiringpi.digitalWrite(IN1+pin, value)
    current_step += 1
    if current_step == step_count:
        current_step = 0
    time.sleep(0.01)