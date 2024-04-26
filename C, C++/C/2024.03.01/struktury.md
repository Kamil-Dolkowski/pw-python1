
#include <stdio.h>

struct vector3D {
    int components[3];
    int size;
};

struct vector3D initV3D(struct vector3D v) {
    v.size = 3;
    return v;
};

int main() {
    struct vector3D v1, v2;
    
    printf("%d\n", v1.size);
    
    v1 = initV3D(v1);
    
    printf("%d\n", v1.size);
    
    return 0; 
}

#---------------------------------------------------------------------------------------------------------------

#include <stdio.h>

struct vector3D {
    int components[3];
    int size;
};

struct vector3D initV3D(struct vector3D v) {
    v.size = 3;
    for (int i=0; i<v.size; i++) {
        v.components[i] = 1;
    }
    return v;
};

int main() {
    struct vector3D v1, v2;
    
    printf("%d\n", v1.size);
    
    v1 = initV3D(v1);
    v2 = initV3D(v2);
    
    printf("%d\n", v1.size);
    
    for (int i=0; i<v1.size; i++) {
        printf("%d ", v1.components[i]);
    }
    
    return 0; 
}

#-------------------------------------------DODAWANIE WEKTORÓW 3D-----------------------------------------------

#include <stdio.h>

//-------------------STRUKTURY---------------------

struct vector3D {
    int components[3];
    int size;
};

struct vector3D initV3D(struct vector3D v) {
    v.size = 3;
    for (int i=0; i<v.size; i++) {
        v.components[i] = 1;
    }
    return v;
};

//-------------------FUNKCJE---------------------

struct vector3D addV3D(struct vector3D x, struct vector3D y) {
    int s;
    struct vector3D z;
    z.size = x.size;
    
    for (s=0; s<z.size; s++) {
        z.components[s] = x.components[s] + y.components[s];
    }
    return z;
} 

void printV3D(struct vector3D v) {
    for (int i=0; i<v.size; i++) {
        printf("%d", v.components[i]);
    }
    printf("\n");
}

//---------------------MAIN----------------------

int main() {
    struct vector3D v1, v2={{4,5,6}, 3}, v;
    
    v1.size = 3;
    v1.components[0] = 1;
    v1.components[1] = 2;
    v1.components[2] = 3;
    
    printV3D(v1);
    printV3D(v2);
    
    
    v = addV3D(v1, v2);
    
    printV3D(v);
    
    return 0; 
}


#-------------------------------------------DODAWANIE WEKTORÓW 2D----------------------------------------------- (*)

#include <stdio.h>

//-------------------STRUKTURY---------------------

struct vector3D {
    int components[3];
    int size;
};

struct vector2D {
    int components[2];
    int size;
};

//-------------------FUNKCJE---------------------

struct vector3D addV3D(struct vector3D x, struct vector3D y) {
    int s;
    struct vector3D z;
    z.size = x.size;
    
    for (s=0; s<z.size; s++) {
        z.components[s] = x.components[s] + y.components[s];
    }
    return z;
} 

void printV3D(struct vector3D v) {
    for (int i=0; i<v.size; i++) {
        printf("%d", v.components[i]);
    }
    printf("\n");
}

struct vector2D addV2D(struct vector2D x, struct vector2D y) {
    int s;
    struct vector2D z;
    z.size = x.size;
    
    for (s=0; s<z.size; s++) {
        z.components[s] = x.components[s] + y.components[s];
    }
    return z;
} 

void printV2D(struct vector2D v) {
    for (int i=0; i<v.size; i++) {
        printf("%d", v.components[i]);
    }
    printf("\n");
}

//---------------------MAIN----------------------

int main() {
    struct vector3D v1, v2={{4,5,6}, 3}, v;
    struct vector2D v1_2D={{1,2}, 2}, v2_2D={{4,5}, 2}, v_2D;
    
    printV2D(v1_2D);
    printV2D(v2_2D);
    
    
    v_2D = addV2D(v1_2D, v2_2D);
    
    printV2D(v_2D);
    
    return 0; 
}

#---------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------