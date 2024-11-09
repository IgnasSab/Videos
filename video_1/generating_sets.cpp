#include <bits/stdc++.h>

using namespace std;


void helper_latex(int n, vector<string>& all_numbers, string str_zero) {

    if (n == 1) {
        all_numbers[0] = str_zero;
        all_numbers[1] = string("\\{") + str_zero + string("\\}");
        return;
    } 

    helper_latex(n - 1, all_numbers, str_zero);

    string str_n_prev = all_numbers[n - 1];
    str_n_prev[str_n_prev.length() - 1] = ',';
    str_n_prev += string(" ");
    all_numbers[n] = str_n_prev + all_numbers[n-1] + string("\\}");

    cout << n << '\n';


}
void helper(int n, vector<string>& all_numbers, string str_zero) {

    if (n == 1) {
        all_numbers[0] = str_zero;
        all_numbers[1] = string("{") + str_zero + string("}");
        return;
    } 

    helper(n - 1, all_numbers, str_zero);

    string str_n_prev = all_numbers[n - 1];
    str_n_prev[str_n_prev.length() - 1] = ',';
    str_n_prev += string(" ");
    all_numbers[n] = str_n_prev + all_numbers[n-1] + string("}");

}

void print_set(vector<string>& all_numbers) {
    int n = all_numbers.size() - 1;
    cout << "{";
    for (int i = 0; i <= n; i++) {
        if (i == n) { cout << all_numbers[i] << "}\n";break;}
        cout << all_numbers[i] << ", ";
    }
}

void fill_file(vector<string>& all_numbers, int char_line) {

    ofstream outFile("natural_numbers_8.txt");

    int char_count = 0;

    int n = all_numbers.size() - 1;
    for (char c : all_numbers[n]) {
        outFile << c;
        if (char_count == char_line) outFile << '\n';
        char_count = (char_count + 1) % (char_line + 1);
    }

}

int count_zeros(vector<string>& all_numbers) {
    int cnt = 0;
    for (string str : all_numbers) {
        for (char c : str) {
            cnt += c == '0';
        }
    }
    return cnt;
}


int main() {

    int n; cin >> n;
    vector<string> all_numbers(n + 1);
    helper(n, all_numbers, "0");
    fill_file(all_numbers, 65);

    // helper_latex(n, all_numbers, "\\emptyset");
    // print_set(all_numbers);



    return 0;
}