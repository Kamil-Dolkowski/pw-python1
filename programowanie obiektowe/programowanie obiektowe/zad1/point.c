#include <stdio.h>
#include <stdlib.h>
#include "point.h"

struct point {
    int x;
    int y;
};


//point_t *point_new(int x, int y);
//void point_free(point_t *p);
//int point_get_x(point_t *p);
//int point_get_y(point_t *p);


point_t *point_new(int x, int y)
{
    point_t *p = malloc(sizeof(struct point));
    p->x = x;
    p->y = y;
    return p;
};

void point_free(point_t *p)
{
    free(p);
};

int point_get_x(point_t *p){
    return p->x;
};

int point_get_y(point_t *p){
    return p->y;
};