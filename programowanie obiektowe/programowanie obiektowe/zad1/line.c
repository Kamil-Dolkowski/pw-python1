#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "point.h"

typedef struct line line_t;

struct line {
    point_t *start;
    point_t *end;
};

//line_t* line_new(point_t *p1, point_t *p2);
//void line_free(line_t *l);
//point_t* line_get_start(line_t *l);
//point_t* line_get_end(line_t *l);
//double line_get_length(line_t *l);

line_t *line_new(point_t *p1, point_t *p2)
{
    line_t *l = malloc(sizeof(struct line));
    l->start = p1;
    l->end = p2;
    return l;
};

void line_free(line_t *l)
{
    free(l);
};
point_t* line_get_start(line_t *l)
{
    return l->start;
};
point_t* line_get_end(line_t *l)
{
    return l->end;
};
double line_get_length(line_t *l)
{
    double length=0;
    int x1, x2, y1, y2;
    point_t *p1, *p2;
    
    p1=line_get_start(l);
    p2=line_get_end(l);
    
    x1=point_get_x(p1);
    y1=point_get_y(p1);
    
    x2=point_get_x(p2);
    y2=point_get_y(p2);
    
    length = sqrt(pow((x2-x1),2)+pow((y2-y1),2));
    return length;
};