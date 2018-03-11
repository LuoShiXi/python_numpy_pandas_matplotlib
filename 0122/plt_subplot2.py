import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

##method 1:subplot2grid
#######################
##plt.figure()
##ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=3)
##ax1.plot([1,2],[1,2])
##ax1.set_title('ax one')

##method 2:gridspec
##
##plt.figure()
##gs = gridspec.GridSpec(3,3)
##ax1 = plt.subplot(gs[1,-2])

##method 3:easy to define structure
###################################
f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,
                                           sharex=True,
                                           sharey=True)
ax11.scatter([1,2],[1,2])




plt.tight_layout()
plt.show()
