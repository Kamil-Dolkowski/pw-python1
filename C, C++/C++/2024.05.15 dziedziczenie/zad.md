
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

#include <iostream>

using namespace std;

class Canvas;

class Line {
  private:
    unsigned int xFrom, yFrom, xTo, yTo;
    char color;
    bool validFrom;
  public:
    Line(unsigned int xTo, unsigned int yTo, char color);
    Line(unsigned int xFrom, unsigned int yFrom, unsigned int xTo, unsigned int yTo, char color);
    void draw(Canvas &canvas);
};

class Canvas {
  private:
    unsigned int x0, y0;
    unsigned int width, height;
    char colorForeground;
    unsigned int xLast, yLast;
    char **cells;
  public:
    Canvas(unsigned int width, unsigned int height);
    Canvas(unsigned int width, unsigned int height, char defaultColor);
    void imageInfo();
    void setColorForeground(char c);
    void moveTo(unsigned int xTo, unsigned int yTo);
    void setPoint(unsigned int x, unsigned int y, char color);
    void setOrigin(unsigned int x, unsigned int y);
    void setLastPoint(unsigned int x, unsigned int y);
};


Canvas::Canvas(unsigned int width, unsigned int height) {
  this -> width = width;
  this -> height = height;
  cells = new char * [width];
  for (int x = 0; x<width; x++) {
    cells[x] = new char[height];
  }
  x0 = 0;
  y0 = 0;
}
    
Canvas::Canvas(unsigned int width, unsigned int height, char defaultColor): Canvas(width, height) {
  for (int x = 0; x<width; x++) {
    for (int y = 0; y<height; y++) {
      cells[x][y] = defaultColor;
    }
  }
}
    
void Canvas::imageInfo() {
  cout << "width=" << width << endl;
  cout << "height=" << height << endl;
  
  for (int y = 0; y<height; y++) {
    for (int x = 0; x<width; x++){
      cout << cells[x][y];
    }
    cout << endl;
  }
}
    
void Canvas::setColorForeground(char c) {
  colorForeground = c;
}

void Canvas::moveTo(unsigned int xTo, unsigned int yTo) {
  xLast = xTo;
  yLast = yTo;
}

void Canvas::setPoint(unsigned int x, unsigned int y, char color) {
  cells[x+x0][y+y0] = color;
}

void Canvas::setOrigin(unsigned int x, unsigned int y) {
  x0 = x;
  y0 = y;
}

void Canvas::setLastPoint(unsigned int x, unsigned int y) {
  xLast = x;
  yLast = y;
}

Line::Line(unsigned int xTo, unsigned int yTo, char color): Line(0, 0, xTo, yTo, color) {
  validFrom = false;
  cout << "fff";
}

Line::Line(unsigned int xFrom, unsigned int yFrom, unsigned int xTo, unsigned int yTo, char color) {
  this->xFrom = xFrom;
  this->yFrom = yFrom;
  this->xTo = xTo;
  this->yTo = yTo;
  this->color = color;
  validFrom = true;
  cout << "eee";
}
  
void Line::draw(Canvas &canvas) {
  unsigned int xF = min(xFrom, xTo);
  unsigned int xT = max(xFrom, xTo);
  
  unsigned int yF = min(yFrom, yTo);
  unsigned int yT = max(yFrom, yTo);
  
  cout <<xFrom<<yFrom<<xTo<<yTo<<endl;
  
  if (xF == xT and yF == yT) { // point
    canvas.setPoint(xF, yF, color);
  }
  else if (xF == xT) { // Vertical line
    for (int y = yF; y<=yT; y++) {
      canvas.setPoint(xF, y, color);
    }
  } else if (yF == yT) { // Horizontal line
    for (int x = xF; x<=xT; x++) {
      canvas.setPoint(x, yF, color);
    }
  } else { // Skew line
    
  }
  
  canvas.setLastPoint(xTo, yTo);
}


int main()
{
  Canvas canvas(15, 10, '.');
  Line l(5,5,10,5,'*');
  
  l.draw(canvas);
  
  canvas.imageInfo();

  return 0;
}

#----------------------------------------------------------------

#include <iostream>

using namespace std;

class Canvas;

class Line {
  private:
    unsigned int xFrom, yFrom, xTo, yTo;
    char color;
    bool validFrom;
  public:
    Line(unsigned int xTo, unsigned int yTo, char color);
    Line(unsigned int xFrom, unsigned int yFrom, unsigned int xTo, unsigned int yTo, char color);
    void draw(Canvas &canvas);
};

class Canvas {
  private:
    unsigned int x0, y0;
    unsigned int width, height;
    char colorForeground;
    unsigned int xLast, yLast;
    char **cells;
  public:
    Canvas(unsigned int width, unsigned int height);
    Canvas(unsigned int width, unsigned int height, char defaultColor);
    ~Canvas();
    void imageInfo();
    void setColorForeground(char c);
    void moveTo(unsigned int xTo, unsigned int yTo);
    void setPoint(unsigned int x, unsigned int y, char color);
    void setOrigin(unsigned int x, unsigned int y);
    void setLastPoint(unsigned int x, unsigned int y);
};


Canvas::Canvas(unsigned int width, unsigned int height) {
  this -> width = width;
  this -> height = height;
  cells = new char * [width];
  for (int x = 0; x<width; x++) {
    cells[x] = new char[height];
  }
  x0 = 0;
  y0 = 0;
}
    
Canvas::Canvas(unsigned int width, unsigned int height, char defaultColor): Canvas(width, height) {
  for (int x = 0; x<width; x++) {
    for (int y = 0; y<height; y++) {
      cells[x][y] = defaultColor;
    }
  }
}

Canvas::~Canvas() {
    cout << "Destructor" << endl;
    for (int x = 0; x<width; x++) {
      delete cells[x];
    }
    delete [] cells;
}
    
void Canvas::imageInfo() {
  cout << "width=" << width << endl;
  cout << "height=" << height << endl;
  
  for (int y = 0; y<height; y++) {
    for (int x = 0; x<width; x++){
      cout << cells[x][y];
    }
    cout << endl;
  }
}
    
void Canvas::setColorForeground(char c) {
  colorForeground = c;
}

void Canvas::moveTo(unsigned int xTo, unsigned int yTo) {
  xLast = xTo;
  yLast = yTo;
}

void Canvas::setPoint(unsigned int x, unsigned int y, char color) {
  cells[x+x0][y+y0] = color;
}

void Canvas::setOrigin(unsigned int x, unsigned int y) {
  x0 = x;
  y0 = y;
}

void Canvas::setLastPoint(unsigned int x, unsigned int y) {
  xLast = x;
  yLast = y;
}

Line::Line(unsigned int xTo, unsigned int yTo, char color): Line(0, 0, xTo, yTo, color) {
  validFrom = false;
  cout << "fff";
}

Line::Line(unsigned int xFrom, unsigned int yFrom, unsigned int xTo, unsigned int yTo, char color) {
  this->xFrom = xFrom;
  this->yFrom = yFrom;
  this->xTo = xTo;
  this->yTo = yTo;
  this->color = color;
  validFrom = true;
  cout << "eee";
}
  
void Line::draw(Canvas &canvas) {
  unsigned int xF = min(xFrom, xTo);
  unsigned int xT = max(xFrom, xTo);
  
  unsigned int yF = min(yFrom, yTo);
  unsigned int yT = max(yFrom, yTo);
  
  cout <<xFrom<<yFrom<<xTo<<yTo<<endl;
  
  if (xF == xT and yF == yT) { // point
    canvas.setPoint(xF, yF, color);
  }
  else if (xF == xT) { // Vertical line
    for (int y = yF; y<=yT; y++) {
      canvas.setPoint(xF, y, color);
    }
  } else if (yF == yT) { // Horizontal line
    for (int x = xF; x<=xT; x++) {
      canvas.setPoint(x, yF, color);
    }
  } else { // Skew line
    
  }
  
  canvas.setLastPoint(xTo, yTo);
}


int main()
{
  Canvas canvas(15, 10, '.');
  Line l(5,5,10,5,'*');
  
  l.draw(canvas);
  
  canvas.imageInfo();

  return 0;
}

#--------------------------PRACA DOMOWA-------------------------- 

PRACA DOMOWA:
-Skew line


..........
..0o......
....oo....
......o0..
..........


#---------------------------------


#include <iostream>
#include <cstdlib>

using namespace std;

class Canvas;

class Line {
  private:
    unsigned int xFrom, yFrom, xTo, yTo;
    char color;
    bool validFrom;
  public:
    Line(unsigned int xTo, unsigned int yTo, char color);
    Line(unsigned int xFrom, unsigned int yFrom, unsigned int xTo, unsigned int yTo, char color);
    void draw(Canvas &canvas);
    
    void plotLineLow(unsigned int xF, unsigned int yF, unsigned int xT, unsigned int yT, Canvas &canvas);
    void plotLineHigh(unsigned int xF, unsigned int yF, unsigned int xT, unsigned int yT, Canvas &canvas);
};

class Canvas {
  private:
    unsigned int x0, y0;
    unsigned int width, height;
    char colorForeground;
    unsigned int xLast, yLast;
    char **cells;
  public:
    Canvas(unsigned int width, unsigned int height);
    Canvas(unsigned int width, unsigned int height, char defaultColor);
    ~Canvas();
    void imageInfo();
    void setColorForeground(char c);
    void moveTo(unsigned int xTo, unsigned int yTo);
    void setPoint(unsigned int x, unsigned int y, char color);
    void setOrigin(unsigned int x, unsigned int y);
    void setLastPoint(unsigned int x, unsigned int y);
};


Canvas::Canvas(unsigned int width, unsigned int height) {
  this -> width = width;
  this -> height = height;
  cells = new char * [width];
  for (int x = 0; x<width; x++) {
    cells[x] = new char[height];
  }
  x0 = 0;
  y0 = 0;
}
    
Canvas::Canvas(unsigned int width, unsigned int height, char defaultColor): Canvas(width, height) {
  for (int x = 0; x<width; x++) {
    for (int y = 0; y<height; y++) {
      cells[x][y] = defaultColor;
    }
  }
}

Canvas::~Canvas() {
    cout << "Destructor" << endl;
    for (int x = 0; x<width; x++) {
      delete cells[x];
    }
    delete [] cells;
}
    
void Canvas::imageInfo() {
  cout << "width=" << width << endl;
  cout << "height=" << height << endl;
  
  for (int y = 0; y<height; y++) {
    for (int x = 0; x<width; x++){
      cout << cells[x][y];
    }
    cout << endl;
  }
}
    
void Canvas::setColorForeground(char c) {
  colorForeground = c;
}

void Canvas::moveTo(unsigned int xTo, unsigned int yTo) {
  xLast = xTo;
  yLast = yTo;
}

void Canvas::setPoint(unsigned int x, unsigned int y, char color) {
  cells[x+x0][y+y0] = color;
}

void Canvas::setOrigin(unsigned int x, unsigned int y) {
  x0 = x;
  y0 = y;
}

void Canvas::setLastPoint(unsigned int x, unsigned int y) {
  xLast = x;
  yLast = y;
}

Line::Line(unsigned int xTo, unsigned int yTo, char color): Line(0, 0, xTo, yTo, color) {
  validFrom = false;
  cout << "fff";
}

Line::Line(unsigned int xFrom, unsigned int yFrom, unsigned int xTo, unsigned int yTo, char color) {
  this->xFrom = xFrom;
  this->yFrom = yFrom;
  this->xTo = xTo;
  this->yTo = yTo;
  this->color = color;
  validFrom = true;
  cout << "eee";
}
  
void Line::draw(Canvas &canvas) {
  unsigned int xF = min(xFrom, xTo);
  unsigned int xT = max(xFrom, xTo);
  
  unsigned int yF = min(yFrom, yTo);
  unsigned int yT = max(yFrom, yTo);
  
  cout <<xFrom<<yFrom<<xTo<<yTo<<endl;
  
  if (xF == xT and yF == yT) { // point
    canvas.setPoint(xF, yF, color);
  }
  else if (xF == xT) { // Vertical line
    for (int y = yF; y<=yT; y++) {
      canvas.setPoint(xF, y, color);
    }
  } else if (yF == yT) { // Horizontal line
    for (int x = xF; x<=xT; x++) {
      canvas.setPoint(x, yF, color);
    }
  } else { // Skew line
  
    // Naive line-drawing algorithm:
    
    /*
    unsigned int dx = xT - xF;
    unsigned int dy = yT - yF;
    
    for (int x=xF; x<=xT; x++) {
        unsigned int y = yF + dy * (x - xF) / dx;
        canvas.setPoint(x, y, color);
    }    
    */
    
    // Bresenham's line algorithm:
    if (abs(int(yT - yF)) < abs(int(xT - xF))) {
        if (xF > xT) {
            plotLineLow(xT, yT, xF, yF, canvas);
        } else {
            plotLineLow(xF, yF, xT, yT, canvas);
        }
    } else {
        if (yF > yT) {
            plotLineHigh(xT, yT, xF, yF, canvas);
        } else {
            plotLineHigh(xF, yF, xT, yT, canvas);
        }
    }
  }
  
  canvas.setLastPoint(xTo, yTo);
}

void Line::plotLineLow(unsigned int xF, unsigned int yF, unsigned int xT, unsigned int yT, Canvas &canvas) {
    int dx = xT - xF;
    int dy = yT - yF;
    int yi = 1;
    if (dy < 0) {
        yi = -1;
        dy = -dy;
    }
    int D = (2 * dy) - dx;
    int y = yF;
    
    for (int x=xF; x<=xT; x++) {
        canvas.setPoint(x, y, color);
        if (D > 0) {
            y = y + yi;
            D = D + (2 * (dy - dx));
        } else {
            D = D + 2*dy;
        }
    }
}

void Line::plotLineHigh(unsigned int xF, unsigned int yF, unsigned int xT, unsigned int yT, Canvas &canvas) {
    int dx = xT - xF;
    int dy = yT - yF;
    int xi = 1;
    if (dx < 0) {
        xi = -1;
        dx = -dx;
    }
    int D = (2 * dx) - dy;
    int x = xF;

    for (int y=yF; y<=yT; y++) {
        canvas.setPoint(x, y, color);
        if (D > 0) {
            x = x + xi;
            D = D + (2 * (dx - dy));
        } else {
            D = D + 2*dx;
        }
    }
}




int main()
{
  Canvas canvas(15, 10, '.');
  Line l(1,1,3,10,'*');
  Line l1(3,10,1,1,'?');
  
  l.draw(canvas);
  l1.draw(canvas);
  
  canvas.imageInfo();

  return 0;
}


