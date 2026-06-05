from fan import Fan

fan1 = Fan()
fan1.set_speed(Fan.FAST)
fan1.set_radius(10)
fan1.set_color("Yellow")
fan1.set_on(True)

fan2 = Fan()
fan2.set_speed(Fan.MEDIUM)
fan2.set_radius(5)
fan2.set_color("Blue")
fan2.set_on(False)

print("\033[32m===== FIRST FAN =====\033[0m")
fan1.display_specs()

print("\n\033[33m===== SECOND FAN =====\033[0m")
fan2.display_specs()
