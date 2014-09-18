from memetics import *
import pygame
import sys

class MemeticSimulationApp(Grid):
    def __init__(self, n):
        self.set_constants()
        Grid.__init__(self, self.cells_per_side)
        pygame.init()
        self.setup_window()
        self.paint()
        self.execute_evolution(n)
        self.wait_for_close()

    def set_constants(self):
        self.cell_size = 10
        self.cells_per_side = 75

    def setup_window(self):
        pygame.display.set_caption("Memetics Simuation")
        pixels_long = self.cells_per_side * self.cell_size
        self.display = pygame.display.set_mode([pixels_long, pixels_long])
        self.display.fill([127, 127, 127])
        
    def paint(self):
        for cell in self:
            pygame.draw.rect(self.display, cell.color,[self.cell_size * cell.c,\
                                                      self.cell_size * cell.r,\
                                                      self.cell_size,\
                                                      self.cell_size])
        pygame.display.flip()
            
    def execute_evolution(self, n = 10):
        pygame.display.set_caption("Memetics Simuation (running)")
        for i in range(n):
            self.paint()
            Grid.execute_evolution(self, 1)
        pygame.display.set_caption("Memetics Simuation (COMPLETE)")

    def wait_for_close(self):
        done = False
        while done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True 
        pygame.quit()


def report_unrecognized_input():
        print "Could not recognize the input number of iterations"
        print "Try entering 'python simulation.py 100'"    

if (len(sys.argv) > 1):
    try:
        app = MemeticSimulationApp(int(sys.argv[1]))
    except:
        report_unrecognized_input()
else:
    report_unrecognized_input()
