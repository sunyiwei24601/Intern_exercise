#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

vector<int> get_color();
void print_vector(vector<int> v);

int main(){
    int num,m,c;
    cin >> num >> m >> c;
    vector<int> *color_list = new vector<int>[num + m -1];
    for (int i = 0; i < num; i++){
        color_list[i] = get_color();
    }
    vector<int> *color_sequence = new vector<int>[c];
    for (int i = 0; i < num; i++){
        for (int color : color_list[i]){
            color_sequence[color - 1].push_back(i + 1);
        }
    }
    for (int i = 0; i < m-1; i++){
            for (int color : color_list[i]){
                color_sequence[color - 1].push_back(i + num + 1);
            }
        }
    

    int wrong_count = 0;
    for (int i=0; i < c; i++){
        int size = color_sequence[i].size();
        for (int j=0; j < size-1; j ++){
            if ((color_sequence[i][j+1] - color_sequence[i][j]) < m){
                wrong_count += 1;
                break;
            }
        }
    }
    cout << wrong_count;

    




    system("pause");


}

vector<int> get_color(){
    int n;
    cin >> n;
    vector <int> colors(n);
    for(int i = 0;i < n; i++){
        cin >> colors[i];
    }
    return colors;

}

void print_vector(vector<int> v){
    for (int i : v){
        cout << i << " ";
    }
    cout << endl;

}

