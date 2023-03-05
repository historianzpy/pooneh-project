import matplotlib.pyplot as plt
names = ['Figma', 'Adobe Xd', 'Adobe Photoshop', 'Adobe Illustrator', 'Canva', 'Blender']
values = [80, 60, 40, 80, 90, 20]

plt.figure(figsize=(12,5))
plt.bar(names, values, width= 0.8, color=['blue', 'green', 'purple', 'red', 'yellow', 'pink'])
plt.suptitle('Skills chart')
plt.show()