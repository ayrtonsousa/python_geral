import matplotlib.pyplot as plt
 
 
def main(args):
    plt.plot([0,1,4,9,16])
    plt.ylabel('Quadrado')
    plt.show()
     
     
    return 0
 
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))