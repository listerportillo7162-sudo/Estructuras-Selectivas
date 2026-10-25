#include <iostream>

using namespace std;

int main() {
    // 1. Declarar la variable para la calificación
    double nota;

    // 2. Solicitar la calificación al usuario
    cout << "Ingrese la nota final del estudiante (0 a 10): ";
    cin >> nota;

    // 3. Estructura selectiva con 'if' y 'else'
    if (nota >= 6.0) {
        cout << "Nota: " << nota << ". El estudiante esta APROBADO." << endl;
    } else {
        cout << "Nota: " << nota << ". El estudiante esta REPROBADO." << endl;
    }

    return 0;
}
