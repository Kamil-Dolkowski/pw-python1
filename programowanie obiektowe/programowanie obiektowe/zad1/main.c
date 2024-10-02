#include <stdio.h>
#include "line.h"
#include "point.h"

int main()
{
    int x,y;
    
    point_t *p1 = point_new(10,20);
    point_t *p2 = point_new(30,40);

    line_t *l1 = line_new(p1,p2);

    printf("Długość linii: %f\n", line_get_length(l1));

    //
    x = point_get_x(p1);
    printf("x p1: %d\n",x);
    y = point_get_y(p1);
    printf("y p1: %d\n",y);
    
    x = point_get_x(p2);
    printf("x p2: %d\n",x);
    y = point_get_y(p2);
    printf("y p2: %d\n",y);
    //

    line_free(l1);
    point_free(p2);
    point_free(p1);

    return 0;
}











