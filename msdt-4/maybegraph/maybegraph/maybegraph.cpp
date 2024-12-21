#include "../packages/glad/include/glad/glad.h"
#include "../packages/glfw.3.3.10/build/native/include/GLFW/glfw3.h"
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
#include <windows.h>
#include <time.h>
#include <string>

// Константа для преобразования градусов в радианы
constexpr float PI = 3.14159265359f;
constexpr float DEG_TO_RAD = 3.14159265359f / 180.0f;
int scr_w;
int scr_h;
// Функция обработки изменения размера окна
void framebuffer_size_callback(GLFWwindow* window, int width, int height) {
    scr_w = width;
    scr_h = height;
    glViewport(0, 0, width, height);
}

// Функция обработки ввода
void processInput(GLFWwindow* window) {
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);
}
struct polygon {
    float vrts[3 * 4];
    float norm[3];
};

/*
    glBegin(GL_LINES);   // Начало отрисовки линий
}*/

// Функция для отрисовки полигона
void drawPolygon(float vertices[4 * 3], float v) {

    glColor3f(v, v, v);  // Установка цвета
    glBegin(GL_POLYGON); // Начало отрисовки полигона

    for (int i = 0; i < 4 * 3; i += 3) {
        if (scr_h > scr_w)
            glVertex2f(2*vertices[i] / (vertices[i + 2] + 2), 2 * vertices[i + 1] * scr_w / scr_h / (vertices[i + 2] + 2));
        else if (scr_w > scr_h)
            glVertex2f(2 * vertices[i] / (vertices[i + 2] + 2) * scr_h / scr_w, 2 * vertices[i + 1] / (vertices[i + 2] + 2));
        else
            glVertex2f(2 * vertices[i] / (vertices[i + 2] + 2), 2 * vertices[i + 1] / (vertices[i + 2] + 2));
    }
    glEnd(); // Конец отрисовки
    glColor3f(0, 0, 0);  // Установка цвета
    glBegin(GL_LINES); // Начало отрисовки полигона

    for (int i = 0; i < 4 * 3; i += 3) {
        if (scr_h > scr_w) {
                glVertex2f(2 * vertices[i] / (vertices[i + 2] + 2), 2 * vertices[i + 1] * scr_w / scr_h / (vertices[i + 2] + 2));
            if(i<3*3)
                glVertex2f(2 * vertices[i+3] / (vertices[i + 2+3] + 2), 2 * vertices[i + 1+3] * scr_w / scr_h / (vertices[i + 2+3] + 2));
            else
                glVertex2f(2 * vertices[i -9] / (vertices[i + 2 -9] + 2), 2 * vertices[i + 1 -9] * scr_w / scr_h / (vertices[i + 2 -9] + 2));
        }
            
        else if (scr_w > scr_h) {
                glVertex2f(2 * vertices[i] / (vertices[i + 2] + 2) * scr_h / scr_w, 2 * vertices[i + 1] / (vertices[i + 2] + 2));
            if (i < 3 * 3)
                glVertex2f(2 * vertices[i+3] / (vertices[i + 2+3] + 2) * scr_h / scr_w, 2 * vertices[i + 1+3] / (vertices[i + 2+3] + 2));
            else
                glVertex2f(2 * vertices[i -9] / (vertices[i + 2 -9] + 2) * scr_h / scr_w, 2 * vertices[i + 1 -9]/ (vertices[i + 2 -9] + 2));
        }
            
        else {
                glVertex2f(2 * vertices[i] / (vertices[i + 2] + 2), 2 * vertices[i + 1] / (vertices[i + 2] + 2));
            if (i < 3 * 3)
                glVertex2f(2 * vertices[i+3] / (vertices[i + 2+3] + 2), 2 * vertices[i + 1+3] / (vertices[i + 2+3] + 2));
            else
                glVertex2f(2 * vertices[i -9] / (vertices[i + 2 -9] + 2), 2 * vertices[i + 1 -9] / (vertices[i + 2 -9] + 2));
        }
            
    }
    glEnd(); // Конец отрисовки
}
/*
void drawPolygon(float vertices[4 * 3], float v) {
    glColor3f(v, v, v);  // Установка цвета
    glBegin(GL_POLYGON); // Начало отрисовки полигона

    for (int i = 0; i < 4 * 3; i += 3) {
        if (scr_h > scr_w)
            glVertex2f(vertices[i], vertices[i + 1] * scr_w / scr_h);
        else if (scr_w > scr_h)
            glVertex2f(vertices[i] * scr_h / scr_w, 2 * vertices[i + 1]);
        else
            glVertex2f(vertices[i] ,vertices[i + 1]);
    }
    glEnd(); // Конец отрисовки
}*/


float cosd(double q) {
    return cos(q * DEG_TO_RAD);
}
float sind(double q) {
    return sin(q * DEG_TO_RAD);
}

float sun_rot[3] = { cosd(45) * cosd(-45),sind(-45),-sind(45) * cosd(-45) };

int debugtime=0;

std::string rettime() {
    int q = time(NULL) - debugtime;
    return std::to_string(q/3600)+std::string(":")+ std::to_string(q/60%60)+ std::string(":") + std::to_string(q%60);
}
int main() {
    debugtime = time(NULL);
    // Инициализация GLFW
    if (!glfwInit()) {
        std::cerr << "Failed to initialize GLFW" << std::endl;
        return -1;
    }
    std::cout << rettime()<<" in main(): GLFW initialized successfully"<<std::endl;
    GLFWwindow* window = glfwCreateWindow(800, 800, "Rotating Polygon", nullptr, nullptr);
    // Настройка окна
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_COMPAT_PROFILE);

    // Создание окна
    if (!window) {
        std::cerr << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }
    std::cout << rettime() << " in main(): GLFW window created successfully"<<std::endl;
    glfwMakeContextCurrent(window);

    // Загрузка функций OpenGL с помощью GLAD
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        std::cerr << "Failed to initialize GLAD" << std::endl;
        return -1;
    }
    std::cout << rettime() << " in main(): GLAD initialized successfully" << std::endl;
    // Установка коллбэка изменения размера окна
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

    const int levels = 16;
    const int slices = levels * 4;
    const int polig_size = slices * levels * 2 + slices;
    const float r = 0.5;
    polygon polygons[polig_size];
    
    //создание киндера
    for (int i = 0;i < slices;i++)
        for (int j = 0;j < levels;j++) {
            polygons[i + j * slices] = {
                {
                    r * cosd(90.0 * (j) / levels) * cosd(360.0 * (i) / slices),
                    0.25f + r * sind(90.0 * (j) / levels),
                    r * cosd(90.0 * (j) / levels) * sind(360.0 * (i) / slices),

                    r * cosd(90.0 * (j + 1) / levels) * cosd(360.0 * (i) / slices),
                    0.25f + r * sind(90.0 * (j + 1) / levels),
                    r * cosd(90.0 * (j + 1) / levels) * sind(360.0 * (i) / slices),

                    r * cosd(90.0 * (j + 1) / levels) * cosd(360.0 * (i + 1) / slices),
                    0.25f + r * sind(90.0 * (j + 1) / levels),
                    r * cosd(90.0 * (j + 1) / levels) * sind(360.0 * (i + 1) / slices),

                    r * cosd(90.0 * (j) / levels) * cosd(360.0 * (i + 1) / slices),
                    0.25f + r * sind(90.0 * (j) / levels),
                    r * cosd(90.0 * (j) / levels) * sind(360.0 * (i + 1) / slices)
                }
                ,
                {
                    cosd(90.0 * (j + 0.5) / levels) * cosd(360.0 * (i + 0.5) / slices),
                    sind(90.0 * (j + 0.5) / levels),
                    cosd(90.0 * (j + 0.5) / levels) * sind(360.0 * (i + 0.5) / slices),
                }
            };
            polygons[i + j * slices + slices * levels] = {
                /*{
                    r * cosd(90.0 * (j) / levels) * cosd(360.0 * (i) / slices),
                    -0.25f + r * sind(90.0 * (j) / levels),
                    r * cosd(90.0 * (j) / levels) * sind(360.0 * (i) / slices),

                    r * cosd(90.0 * (j + 1) / levels) * cosd(360.0 * (i) / slices),
                    -0.25f + r * sind(90.0 * (j + 1) / levels),
                    r * cosd(90.0 * (j + 1) / levels) * sind(360.0 * (i) / slices),

                    r * cosd(90.0 * (j + 1) / levels) * cosd(360.0 * (i + 1) / slices),
                    -0.25f + r * sind(90.0 * (j + 1) / levels),
                    r * cosd(90.0 * (j + 1) / levels) * sind(360.0 * (i + 1) / slices),

                    r * cosd(90.0 * (j) / levels) * cosd(360.0 * (i + 1) / slices),
                    -0.25f + r * sind(90.0 * (j) / levels),
                    r * cosd(90.0 * (j) / levels) * sind(360.0 * (i + 1) / slices)
                }
                ,
                {
                    -cosd(90.0 * (j + 0.5) / levels) * cosd(360.0 * (i + 0.5) / slices),
                    -sind(90.0 * (j + 0.5) / levels),
                    -cosd(90.0 * (j + 0.5) / levels) * sind(360.0 * (i + 0.5) / slices),
                }*/
                {
                    r * cosd(90.0 * (j) / levels) * cosd(360.0 * (i) / slices),
                    -0.25f - r * sind(90.0 * (j) / levels),
                    r * cosd(90.0 * (j) / levels) * sind(360.0 * (i) / slices),

                    r * cosd(90.0 * (j + 1) / levels) * cosd(360.0 * (i) / slices),
                    -0.25f - r * sind(90.0 * (j + 1) / levels),
                    r * cosd(90.0 * (j + 1) / levels) * sind(360.0 * (i) / slices),

                    r * cosd(90.0 * (j + 1) / levels) * cosd(360.0 * (i + 1) / slices),
                    -0.25f - r * sind(90.0 * (j + 1) / levels),
                    r * cosd(90.0 * (j + 1) / levels) * sind(360.0 * (i + 1) / slices),

                    r * cosd(90.0 * (j) / levels) * cosd(360.0 * (i + 1) / slices),
                    -0.25f - r * sind(90.0 * (j) / levels),
                    r * cosd(90.0 * (j) / levels) * sind(360.0 * (i + 1) / slices)
                }
                ,
                {
                    cosd(90.0 * (j + 0.5) / levels) * cosd(360.0 * (i + 0.5) / slices),
                    -sind(90.0 * (j + 0.5) / levels),
                    cosd(90.0 * (j + 0.5) / levels) * sind(360.0 * (i + 0.5) / slices),
                }
            };
        }
    for (int i = 0;i < slices;i++) {
        polygons[i + slices * levels * 2] = {
                {
                    r * cosd(360.0 * (i) / slices),
                    -0.25f,
                    r * sind(360.0 * (i) / slices),

                    r * cosd(360.0 * (i) / slices),
                    0.25f,
                    r * sind(360.0 * (i) / slices),

                    r * cosd(360.0 * (i + 1) / slices),
                    0.25f,
                    r * sind(360.0 * (i + 1) / slices),

                    r * cosd(360.0 * (i + 1) / slices),
                    -0.25f,
                    r * sind(360.0 * (i + 1) / slices)
                }
                ,
                {
                    cosd(360.0 * (i + 0.5) / slices),
                    0,
                    sind(360.0 * (i + 0.5) / slices),
                }
        };
    }

    std::cout << rettime() << " in main(): figure built successfully" << std::endl;
    float sunr = 0;
    float scale = 1;
    float shift = 0;

    bool nottrashing = false;
    bool frame90noticed = false;
    // Основной цикл
    while (!glfwWindowShouldClose(window)) {
        processInput(window);
        if ((int)sunr % 90==0 && !nottrashing && !frame90noticed)
            nottrashing = true;
        // Очистка экрана
        glClearColor(0.1f, 0.1f, 0.1f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);
        if(nottrashing)
            std::cout << rettime() << " in main(): now sun rotated on 90d: GL buffer cleared" << std::endl;

        polygon transformed_polygons[polig_size];

        for (int qpolig = 0;qpolig < polig_size;qpolig++) {
            float x1 = polygons[qpolig].vrts[0];
            float y1 = polygons[qpolig].vrts[1];
            float z1 = polygons[qpolig].vrts[2];
            float x2 = polygons[qpolig].vrts[3];
            float y2 = polygons[qpolig].vrts[4];
            float z2 = polygons[qpolig].vrts[5];
            float x3 = polygons[qpolig].vrts[6];
            float y3 = polygons[qpolig].vrts[7];
            float z3 = polygons[qpolig].vrts[8];
            float x4 = polygons[qpolig].vrts[9];
            float y4 = polygons[qpolig].vrts[10];
            float z4 = polygons[qpolig].vrts[11];
            float xn = polygons[qpolig].norm[0];
            float yn = polygons[qpolig].norm[1];
            float zn = polygons[qpolig].norm[2];
            transformed_polygons[qpolig] = {
                {
                x1,
                y1 * cosd(sunr) - z1 * sind(sunr),
                y1 * sind(sunr) + z1 * cosd(sunr),

                x2,
                y2 * cosd(sunr) - z2 * sind(sunr),
                y2 * sind(sunr) + z2 * cosd(sunr),

                x3,
                y3 * cosd(sunr) - z3 * sind(sunr),
                y3 * sind(sunr) + z3 * cosd(sunr),

                x4,
                y4 * cosd(sunr) - z4 * sind(sunr),
                y4 * sind(sunr) + z4 * cosd(sunr)
                },
                {
                    xn,
                    yn * cosd(sunr) - zn * sind(sunr),
                    yn * sind(sunr) + zn * cosd(sunr),
                }
            };
            x1 = transformed_polygons[qpolig].vrts[0];
            y1 = transformed_polygons[qpolig].vrts[1];
            z1 = transformed_polygons[qpolig].vrts[2];
            x2 = transformed_polygons[qpolig].vrts[3];
            y2 = transformed_polygons[qpolig].vrts[4];
            z2 = transformed_polygons[qpolig].vrts[5];
            x3 = transformed_polygons[qpolig].vrts[6];
            y3 = transformed_polygons[qpolig].vrts[7];
            z3 = transformed_polygons[qpolig].vrts[8];
            x4 = transformed_polygons[qpolig].vrts[9];
            y4 = transformed_polygons[qpolig].vrts[10];
            z4 = transformed_polygons[qpolig].vrts[11];
            xn = transformed_polygons[qpolig].norm[0];
            yn = transformed_polygons[qpolig].norm[1];
            zn = transformed_polygons[qpolig].norm[2];
            transformed_polygons[qpolig] = { {
                x1 * cosd(sunr) + z1 * sind(sunr),
                y1,
                -x1 * sind(sunr) + z1 * cosd(sunr),


                x2 * cosd(sunr) + z2 * sind(sunr),
                y2,
                -x2 * sind(sunr) + z2 * cosd(sunr),


                x3 * cosd(sunr) + z3 * sind(sunr),
                y3,
                -x3 * sind(sunr) + z3 * cosd(sunr),


                x4 * cosd(sunr) + z4 * sind(sunr),
                y4,
                -x4 * sind(sunr) + z4 * cosd(sunr),
                },
                {

                xn * cosd(sunr) + zn * sind(sunr),
                yn,
                -xn * sind(sunr) + zn * cosd(sunr),
                }
                
            };
            x1 = transformed_polygons[qpolig].vrts[0];
            y1 = transformed_polygons[qpolig].vrts[1];
            z1 = transformed_polygons[qpolig].vrts[2];
            x2 = transformed_polygons[qpolig].vrts[3];
            y2 = transformed_polygons[qpolig].vrts[4];
            z2 = transformed_polygons[qpolig].vrts[5];
            x3 = transformed_polygons[qpolig].vrts[6];
            y3 = transformed_polygons[qpolig].vrts[7];
            z3 = transformed_polygons[qpolig].vrts[8];
            x4 = transformed_polygons[qpolig].vrts[9];
            y4 = transformed_polygons[qpolig].vrts[10];
            z4 = transformed_polygons[qpolig].vrts[11];
            xn = transformed_polygons[qpolig].norm[0];
            yn = transformed_polygons[qpolig].norm[1];
            zn = transformed_polygons[qpolig].norm[2];
            transformed_polygons[qpolig] = { {
                x1 * scale,
                y1* scale,
                z1* scale,


                x2* scale,
                y2* scale,
                z2* scale,


                x3* scale,
                y3* scale,
                z3* scale,


                x4* scale,
                y4* scale,
                z4* scale,
                },
                {

                xn,
                yn,
                zn,
                }

            };
            x1 = transformed_polygons[qpolig].vrts[0];
            y1 = transformed_polygons[qpolig].vrts[1];
            z1 = transformed_polygons[qpolig].vrts[2];
            x2 = transformed_polygons[qpolig].vrts[3];
            y2 = transformed_polygons[qpolig].vrts[4];
            z2 = transformed_polygons[qpolig].vrts[5];
            x3 = transformed_polygons[qpolig].vrts[6];
            y3 = transformed_polygons[qpolig].vrts[7];
            z3 = transformed_polygons[qpolig].vrts[8];
            x4 = transformed_polygons[qpolig].vrts[9];
            y4 = transformed_polygons[qpolig].vrts[10];
            z4 = transformed_polygons[qpolig].vrts[11];
            xn = transformed_polygons[qpolig].norm[0];
            yn = transformed_polygons[qpolig].norm[1];
            zn = transformed_polygons[qpolig].norm[2];
            transformed_polygons[qpolig] = { {
                x1+shift,
                y1,
                z1,


                x2+shift,
                y2,
                z2,


                x3+shift,
                y3,
                z3,


                x4+shift,
                y4,
                z4,
                },
                {

                xn,
                yn,
                zn,
                }

            };
        }
        if (nottrashing)
            std::cout << rettime() << " in main(): now sun rotated on 90d: figure transform completed" << std::endl;
        std::sort(std::begin(transformed_polygons), std::end(transformed_polygons),
            [](const polygon& a, const polygon& b) {
                return (a.vrts[2] + a.vrts[5] + a.vrts[8] + a.vrts[11]) / 4 > (b.vrts[2] + b.vrts[5] + b.vrts[8] + b.vrts[11]) / 4; // Сравнение на основе z-координаты
            });
        if (nottrashing)
            std::cout << rettime() << " in main(): now sun rotated on 90d: polygons sorted to z coordinate to camera" << std::endl;
        for (int i = 0;i < polig_size;i++) {
            float xp = transformed_polygons[i].norm[0];
            float yp = transformed_polygons[i].norm[1];
            float zp = transformed_polygons[i].norm[2];
            float v = xp * sun_rot[0] + yp * sun_rot[1] + zp * sun_rot[2];
            /*float xq = (transformed_polygons[i].vrts[0] + transformed_polygons[i].vrts[3] + transformed_polygons[i].vrts[6] + transformed_polygons[i].vrts[9]) / 4;
            float yq = (transformed_polygons[i].vrts[1] + transformed_polygons[i].vrts[4] + transformed_polygons[i].vrts[7] + transformed_polygons[i].vrts[10]) / 4;
            float zq = (transformed_polygons[i].vrts[2] + transformed_polygons[i].vrts[5] + transformed_polygons[i].vrts[8] + transformed_polygons[i].vrts[11]) / 4+2;
            float sq = sqrt(xq*xq+yq*yq+zq*zq);
            xq /= sq;
            yq /= sq;
            zq /= sq;
            float q = xp * xq + yp * yq + zp * zq;
            xq -= 2 * xp * q;
            yq -= 2 * yp * q;
            zq -= 2 * zp * q;
            q+= xq * sun_rot[0] + yq * sun_rot[1] + zq * sun_rot[2];
            if (q > 0.9)
                v = 1;*/
            if(transformed_polygons[i].norm[2]<=0)
            drawPolygon(transformed_polygons[i].vrts, 0.5 - v / 2);
        }
        if (nottrashing)
            std::cout << rettime() << " in main(): now sun rotated on 90d: polygons drawing completed" << std::endl;
        sun_rot[0] = cosd(sunr) * cosd(-45);
        sun_rot[1] = sind(-45);
        sun_rot[2] = -sind(sunr) * cosd(-45);
        sunr += 0.1;
        scale = sind(sunr*4)/4+0.75;
        shift = sind(sunr);

        if (nottrashing)
            std::cout << rettime() << " in main(): now sun rotated on 90d: all variables updated to next frame" << std::endl;
        /*drawLines({
     cos(a*DEG_TO_RAD),  sin(a * DEG_TO_RAD),
     cos((a+90) * DEG_TO_RAD), sin((a+90) * DEG_TO_RAD),
     cos((a + 90) * DEG_TO_RAD), sin((a + 90) * DEG_TO_RAD),
     cos((a + 180) * DEG_TO_RAD), sin((a + 180) * DEG_TO_RAD),
     cos((a + 180) * DEG_TO_RAD), sin((a + 180) * DEG_TO_RAD),
     cos((a + 180+90) * DEG_TO_RAD), sin((a + 180+90) * DEG_TO_RAD),
     cos((a + 180 + 90) * DEG_TO_RAD), sin((a + 180 + 90) * DEG_TO_RAD),
     cos((a) * DEG_TO_RAD), sin((a) * DEG_TO_RAD),
            }
        ,0.8f, 0.2f, 0.2f);
        drawLines(polygonVertices, 1.0, 1.0, 1.0);*/

        // Смена буферов
        glfwSwapBuffers(window);
        glfwPollEvents();
        if (nottrashing)
            std::cout << rettime() << " in main(): now sun rotated on 90d: frame updated; frame cycle is done." << std::endl<<std::endl;

        if ((int)sunr % 90 == 45)
            frame90noticed = false;
        if (nottrashing) {
            nottrashing = false;
            frame90noticed = true;
        }

        
        
            
    }

    glfwTerminate();
    return 0;
}
