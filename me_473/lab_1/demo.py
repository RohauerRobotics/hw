# Python code from ME 473 class
import board, analogio, time

A2_pin = analogio.AnalogIn(board.A2) # analog input
print(A2_pin.value)
# 65536 - 16 bit binary value of analog reading 2^16
A2_V =  (A2_pin.value / 65536) * 3.3 # 
print(A2_V)

def get_voltage(pin):
	return pin.value/65536 * 3.3

print(get_voltage(A2_pin))

# Repeatedly take measurements until t_final

t_final = 1 # final time in seconds

t0 = time.monotonic_ns() # time is defined in nanoseconds
# monotonic prevents time from circling back to zero
while True:
	# define time in seconds
	t = (time.monotonic_ns() - t0)*10**-9
	if t > t_final:
		break
	print(get_voltage(A2_pin))
	time.sleep(0.1) # seconds