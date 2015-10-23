
datavar <- read.csv('C:/Python27/TwitterTrainU.csv')
attach(datavar)
datavar
st = data.frame(datavar)
summary(st)
cor(st)
pairs(st)

model1 = lm(formula = FOLLOWERS ~ FOLLOWING + STATUSES + DAYS + LISTED, data = datavar)

model2 = lm(formula = FOLLOWERS ~ FOLLOWING + LISTED, data = datavar)

model3 = lm(formula = FOLLOWERS ~  LISTED, data = datavar)


step(model1, direction="backward")

confint(model1)


 par(mfrow=c(2,2))                    # visualize four graphs at once
 plot(model1)
 par(mfrow=c(1,1)) 



 



