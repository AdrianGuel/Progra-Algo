out=sim('noisysignal',10);
t=out.noisysignal.time;
y=out.noisysignal.signals.values;
data=[t y];
csvwrite('noisysignalfile.csv',data)
plot(t,y)
