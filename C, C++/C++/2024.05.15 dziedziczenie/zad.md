
obraz rastrowy, pikselowy

#----------------------------------------------------------------

#include <iostream>
using namespace std;

class Canvas {
private:
    unsigned int width, height;
    char **cells;
public:
    Canvas(unsigned int width, unsigned int height) {
        this -> width = width;
        this -> height = height;
        
        cells = new char * [width];
        for (int x=0; x<width; x++) {
            cells[x] = new char [height];
        }
    }

    Canvas(unsigned int width, unsigned int height, char defaultColor): Canvas(width, height) {
        for (int x=0; x<width; x++) {
            for (int y=0; y<height; y++) {
                cells[x][y] = defaultColor;
            }
        }
    }

    void imageInfo() {
        cout << "width=" << width << endl;
        cout << "height=" << height << endl;
        
        for (int y=0; y<height; y++) {
            for (int x=0; x<width; x++) {
                cout << cells[x][y];
            }
            cout << endl;
        }
    }
};


int main()
{
    Canvas canvas(10,5,'.');
    canvas.imageInfo();
    
    return 0;
}

#-----------------------------LINIA------------------------------

#include <iostream>
using namespace std;

class Canvas {
private:
    unsigned int width, height;
    char colorForeground;
    char **cells;
public:
    Canvas(unsigned int width, unsigned int height) {
        this -> width = width;
        this -> height = height;
        
        cells = new char * [width];
        for (int x=0; x<width; x++) {
            cells[x] = new char [height];
        }
    }
    
    Canvas(unsigned int width, unsigned int height, char defaultColor): Canvas(width, height) {
        for (int x=0; x<width; x++) {
            for (int y=0; y<height; y++) {
                cells[x][y] = defaultColor;
            }
        }
    }
    
    void imageInfo() {
        cout << "width=" << width << endl;
        cout << "height=" << height << endl;
        
        for (int y=0; y<height; y++) {
            for (int x=0; x<width; x++) {
                cout << cells[x][y];
            }
            cout << endl;
        }
    }
    
    void setColorForeground(char c) {
        colorForeground = c;
    }
    
    void line(unsigned int xFrom, unsigned int yFrom, unsigned int xTo, unsigned int yTo) {
        if (xFrom == xTo and yFrom == yTo) { // Point
            cells[xFrom][yFrom] = colorForeground;
        }
        if (xFrom == xTo) { // Vertical line
            for (int y=yFrom; y<=yTo; y++) {
                cells[xFrom][y] = colorForeground;
            }
        } else if (yFrom == yTo) { // Horizontal line
            for (int x=xFrom; x<=xTo; x++) {
                cells[x][yFrom] = colorForeground;
            }
        } else { // Skew line
            
        }
    }
};


int main()
{
    Canvas canvas(10,5,'.');
    canvas.imageInfo();
    
    canvas.setColorForeground('*');
    canvas.line(1,1,1,1);
    canvas.imageInfo();
    
    canvas.line(1,4,9,4);
    canvas.imageInfo();
    
    canvas.line(0,1,6,1);
    canvas.imageInfo();
    
    return 0;
}

#----------------------------------------------------------------

#include <iostream>
using namespace std;

class Canvas {
private:
    unsigned int width, height;
    char colorForeground;
    char **cells;
public:
    Canvas(unsigned int width, unsigned int height) {
        this -> width = width;
        this -> height = height;
        
        cells = new char * [width];
        for (int x=0; x<width; x++) {
            cells[x] = new char [height];
        }
    }
    
    Canvas(unsigned int width, unsigned int height, char defaultColor): Canvas(width, height) {
        for (int x=0; x<width; x++) {
            for (int y=0; y<height; y++) {
                cells[x][y] = defaultColor;
            }
        }
    }
    
    void imageInfo() {
        cout << "width=" << width << endl;
        cout << "height=" << height << endl;
        
        for (int y=0; y<height; y++) {
            for (int x=0; x<width; x++) {
                cout << cells[x][y];
            }
            cout << endl;
        }
    }
    
    void setColorForeground(char c) {
        colorForeground = c;
    }
    
    void line(unsigned int xFrom, unsigned int yFrom, unsigned int xTo, unsigned int yTo) {
        line(xFrom, yFrom, xTo, yTo, colorForeground);
    }
    
    void line(unsigned int xFrom, unsigned int yFrom, unsigned int xTo, unsigned int yTo, char color) {
        unsigned int xF, xT, yF, yT;
        
        xF = min(xFrom, xTo);
        xT = max(xFrom, xTo);
        
        yF = min(yFrom, yTo);
        yT = max(yFrom, yTo);
        
        if (xF == xT and yF == yT) { // Point
            cells[xF][yF] = color;
        } else if (xF == xT) { // Vertical line
            for (int y=yF; y<=yT; y++) {
                cells[xF][y] = color;
            }
        } else if (yF == yT) { // Horizontal line
            for (int x=xF; x<=xT; x++) {
                cells[x][yF] = color;
            }
        } else { // Skew line
            
        }
    }
};


int main()
{
    Canvas canvas(15,10,'.');
    
    canvas.setColorForeground('*');
    canvas.line(3,1,7,1);
    
    canvas.setColorForeground('#');
    canvas.line(7,1,7,6);
    
    canvas.line(7,7,3,7,'@');
    canvas.line(3,1,3,7,'%');
    canvas.imageInfo();
    

  
    return 0;
}

#---------------------------------------------------------------- 

#include <iostream>
using namespace std;

class Canvas {
private:
    unsigned int width, height;
    char colorForeground;
    unsigned int xLast, yLast;
    char **cells;
public:
    Canvas(unsigned int width, unsigned int height) {
        this -> width = width;
        this -> height = height;
        
        cells = new char * [width];
        for (int x=0; x<width; x++) {
            cells[x] = new char [height];
        }
    }
    
    Canvas(unsigned int width, unsigned int height, char defaultColor): Canvas(width, height) {
        for (int x=0; x<width; x++) {
            for (int y=0; y<height; y++) {
                cells[x][y] = defaultColor;
            }
        }
    }
    
    void imageInfo() {
        cout << "width=" << width << endl;
        cout << "height=" << height << endl;
        
        for (int y=0; y<height; y++) {
            for (int x=0; x<width; x++) {
                cout << cells[x][y];
            }
            cout << endl;
        }
    }
    
    void setColorForeground(char c) {
        colorForeground = c;
    }
    
    void line(unsigned int xFrom, unsigned int yFrom, unsigned int xTo, unsigned int yTo) {
        line(xFrom, yFrom, xTo, yTo, colorForeground);
    }
    
    void line(unsigned int xFrom, unsigned int yFrom, unsigned int xTo, unsigned int yTo, char color) {
        unsigned int xF, xT, yF, yT;
        
        xF = min(xFrom, xTo);
        xT = max(xFrom, xTo);
        
        yF = min(yFrom, yTo);
        yT = max(yFrom, yTo);
        
        if (xF == xT and yF == yT) { // Point
            cells[xF][yF] = color;
        } else if (xF == xT) { // Vertical line
            for (int y=yF; y<=yT; y++) {
                cells[xF][y] = color;
            }
        } else if (yF == yT) { // Horizontal line
            for (int x=xF; x<=xT; x++) {
                cells[x][yF] = color;
            }
        } else { // Skew line
            
        }
        
        xLast = xTo;
        yLast = yTo;
        
        colorForeground = color;
    }
    
    void line(unsigned int xTo, unsigned int yTo) {
        line(xLast, yLast, xTo, yTo, colorForeground);
    }
    
    void line(unsigned int xTo, unsigned int yTo, char color) {
        line(xLast, yLast, xTo, yTo, color);
    }

};


int main()
{
    Canvas canvas(15,10,'.');
    
    canvas.setColorForeground('*');
    canvas.line(3,1,7,1);
    
    canvas.setColorForeground('#');
    canvas.line(7,1,7,6);
    
    canvas.line(7,7,3,7,'@');
    canvas.line(9,2,12,2,'+');
    canvas.line(12,9);
    canvas.imageInfo();
    

  
    return 0;
}

#----------------------------------------------------------------



#----------------------------------------------------------------



#----------------------------------------------------------------



PRACA DOMOWA:
-Skew line






..........
..0o......
....oo....
......o0..
..........


