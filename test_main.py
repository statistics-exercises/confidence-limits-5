import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_n_uniform_discrete(self) :
        for n in range(2,4) : 
            for a in range(1,3) :
                for b in range(6,7) : 
                    mean = 0
                    for i in range(10) : 
                        var = n_uniform_discrete(n,a,b)
                        self.assertTrue( np.fabs( np.floor(var) - var)<1e-7, "your function n_uniform_discrete returns a number that is not an integer" )
                        self.assertTrue( var>=n*a and var<=n*b, "your function n_uniform_discrete returns a number that falls outside the permitted range" )
                        mean = mean + var
                    mean = mean / 10
                    var = n/12*( (b-a+1)*(b-a+1) - 1 )
                    bar = np.sqrt(var/10)*st.norm.ppf( (0.99 + 1) / 2 )
                    self.assertTrue( np.fabs( mean - n*0.5*(b+a) )<bar, "your function n_uniform_discrete appears to be sampling from the wrong distribution" )
                    
    def test_xplot(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        for i in range( len(this_x) ) :
             self.assertTrue( np.abs(i+1 - this_x[i])<1e-7, "the x-coordinates in your graph are incorrect" )
             
    def test_plot(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        var = myn*( (myb-mya+1)*(myb-mya+1) - 1 ) / 12 
        bar = np.sqrt(var/mym)*st.norm.ppf( (0.99 + 1) / 2 )
        for y in this_y : self.assertTrue( np.fabs( y - 0.5*myn*(myb+mya) )<bar, "the resampled random variables that are plotted on your graph appear to be sampled from the wrong distribution"  )
