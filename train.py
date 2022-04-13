from trainerClass import *

T1 = Trainer("data.csv")
T1.setLearningRate()
for i in range(1000):
    T1.train()
T1.denormalize()

plt.scatter(T1.mileage, T1.price)
plt.title('The car price vs mileage', fontsize=20)
plt.xlabel('mileage', fontsize=18)
plt.ylabel('price', fontsize=18)
# plt.ylim(ymin=0)
plt.xlim(xmin=0)
x = np.array(range(240000))
y = T1.theta0 + T1.theta1 * x

plt.plot(x, y)

plt.show()

