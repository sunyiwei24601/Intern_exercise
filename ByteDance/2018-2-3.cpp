#include<iostream>
#include<vector>
using namespace std;

int sum_up(int i);
void print_vector(vector<int> v);

int main(){
    vector <int> * character_list = new vector<int>[26];

    char c = cin.get();
    int cc = c;
    int position = 0;
    while(cc != 32 ){
        //cout << cc << endl;
        cc -= 97;
        character_list[cc].push_back(position);
        position += 1;
        cc = (int) cin.get();
    }

    int m;
    cin >> m;
    for (int i = 0; i < 26; i++)
        print_vector(character_list[i]);
    int max_num = 0;
    int left_count = 0;
    int right_count = 0;
    int center, length, center_number, total_count;

    for (int i = 0; i < 26; i++){
        //check -left
        length = character_list[i].size();
        if (length == 0)
            continue;
        total_count = 0;
        if (length % 2 == 0){
            center = length/2;
        }
        else{
            center = (length + 1)/2 - 1;
        }
        center_number = character_list[i][center];
        
        left_count = 0;
        for ( int left_position = 0; left_position < center; left_position ++){
            left_count += (center_number - character_list[i][left_position]);
        }
        cout << left_count << " ";
        
        left_count -= sum_up(length/2);

        right_count = 0;
        for (int right_position = center + 1; right_position < length; right_position++){
            right_count += (character_list[i][right_position] - center_number);
        }

        right_count -= sum_up(length - length/2 - 1);

        cout << right_count << endl;
        cout << left_count << " " << right_count<< endl;
        total_count = right_count + left_count;
        if (total_count > max_num){
            max_num = total_count;
        }

    }
    cout << max_num;

    system("pause");


}


int sum_up(int i){
    int result = 0;
    for (int j = 1; j <= i; j ++){
        result += j; 
    }
    return result;
}

void print_vector(vector<int> v){
    for (int i : v){
        cout << i << " ";
    }
    cout << endl;

}