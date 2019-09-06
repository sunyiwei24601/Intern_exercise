#include<iostream>
#include<vector>
#include<string>
using namespace std;

bool check_vector_last3(vector <char>);
bool check_vector_last4(vector <char>);
void print_vector(vector <char>);
void word_process(string);

int main(){
    int num;
    cin >> num;
    string current_word;
    
    for (int i = 0; i < num; i++)
        cin >> current_word;
        cout << current_word <<endl;
        word_process(current_word);
    
    

    system("pause");

    

}


void word_process(string current_word){
    
    int length = current_word.size();
    vector <char> result (1);
    result[0] = current_word[0];
    if (length > 2){
        result[1] = current_word[1];
    }
    else{
        cout << current_word;
    }
    result.push_back(current_word[2]);
    if (check_vector_last3(result)){
        result.pop_back();
    }
    for (int i = 3; i < length; i++){
        result.push_back(current_word[i]);
        if (check_vector_last3(result)){
            result.pop_back();
            continue;
        }
        if (check_vector_last4(result)){
            result.pop_back();
        }

    }
    print_vector(result);






    }




bool check_vector_last3(vector<char> v){
    int length = v.size();
    int last = length - 1;
    if ((v[last] == v[last - 1]) && (v[last - 1] == v[last -2]) ){
        return true;
    }
    else{
        return false;
    }
}
bool check_vector_last4(vector<char> v){
    int length = v.size();
    int last = length - 1;
    if ((v[last] == v[last - 1]) && (v[last-2] == v[last-3])){
        return true;
    }
    return false;
}

void print_vector(vector<char> v){
    for (char i : v){
        cout << i;
    }
    cout << endl;

}