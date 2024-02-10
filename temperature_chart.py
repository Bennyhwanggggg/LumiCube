"""
Chart the temperature of the cube on the screen.
Note: Requires the advanced kit screen module and interactive add-on.
"""
import matplotlib.pyplot as plt


file_name = "Chart.jpg"
temperatures = [0 for i in range(0,20)]
while True:
    temperatures.pop(0)
    temperatures.append(env_sensor.temperature)
    fig = plt.figure(figsize=(3.20, 2.40*0.8))
    times = [i for i in range(0,20)] # plot 20 minutes
    plt.plot(times, temperatures, label = "Temp")
    plt.xlabel('Time (minutes)')
    plt.legend()
    fig.savefig(file_name, bbox_inches='tight')
    screen.draw_image(file_name)
    time.sleep(60)
