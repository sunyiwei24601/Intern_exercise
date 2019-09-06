#include<iostream>
#include<vector>
using namespace std;

int main(){
    int num;
    cin >> num;
    const int s = num;
    vector <int> search_list(num);
    for (int i=0; i < num; i++){
        int number;
        cin >> number;
        search_list[i] = number;
    }
    int search_times;
    cin >> search_times;
    for (int i=0; i < search_times; i++){
        int start;
        cin >> start;
        int end;
        cin >> end;
        int k;
        cin >> k;
        int count = 0;
        //cout << start <<" " << end<<" " << k<<" " << endl;
        for (int j = start - 1; j < end; j++){
          //  cout << search_list[j] <<" ";
            if (search_list[j] == k)
                count += 1;
        }
        //cout << endl;
        cout << count << endl;
    }




    //system("pause");
    return 0;
}