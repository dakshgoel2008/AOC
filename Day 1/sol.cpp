/**
    author:  UG_BEAST
**/

#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define fastio() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define all(v) v.begin(), v.end()
#define pb push_back

vector<string> lines;

vector<string> split(string s, char delimiter) {
	vector<string> tokens;
	string token;
	istringstream tokenStream(s);
	while (getline(tokenStream, token, delimiter)) {
		tokens.push_back(token);
	}
	return tokens;
}

////////////////////////// SOLUTION //////////////////////////

void part1() {
	ll c = 50;
	ll hits = 0;
	for (auto s : lines) {
		char dir = s[0];
		ll val = stoll(s.substr(1));
		if (dir == 'R') c = (c + val) % 100;
		else c = (c - val) % 100;

		if (c < 0) c += 100;
		if (c == 0) hits++;
	}
	cout << "Part1: " << hits << endl;
}

void part2() {
	ll c = 50;
	ll hits = 0;
	for (auto s : lines) {
		char dir = s[0];
		int dkg = 0;		// current hits.
		ll val = stoll(s.substr(1));
		if (dir == 'R') {
			dkg = (c + val) / 100 - (c / 100);
			hits += dkg;
			c = (c + val) % 100;
		} else {
			dkg = floor((double)(c - 1) / 100) - floor((double)(c - 1 - val) / 100);
			hits += dkg;
			c = (c - val) % 100;
		}
		if (c < 0) c += 100;
	}
	cout << "Part2: " << hits << endl;
}

//////////////////////// SOLUTION ENDS //////////////////////////

void solve() {
	string line;
	while (getline(cin, line)) {
		if (!line.empty()) lines.pb(line);
	}

	part1();
	part2();
}

int main() {
	fastio();
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	freopen("Error.txt", "w", stderr);
#endif

	solve();

	return 0;
}