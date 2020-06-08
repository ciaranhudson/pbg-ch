install.packages('MASS')
library(MASS)

attach(Traffic)

?Traffic


help(Traffic)
str(Traffic)


boxplot(limit, y, main="Speed Limit vs Accident Count", ylab ="accident count", xlab = "speed limit")
