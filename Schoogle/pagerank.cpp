#include <iostream> 
#include <libpg>
#include <string>
#include <vector>

using namespace std;

#define DAMPENING_FACTOR = 0.85

// so to use this we are going to need to create the following methods to be able to tap into our DB
float getPR(string url);

//
void getInLinks(string url,vector<string> &);

//
bool updatePR(string url, float pr);

//
int getTableSize(string Table)

// this needs to be able to get the next url entry, hopefully there is some sort of Posgresql buffer object
// that makes this easy to implement
string getNext();

bool Calculate_Rank(double delta, string Rank_Table){
	bool satisfied = true;
	vector<string> links_Vector
	string url;
	float pr;
	while(satisfied){

		for(int i = 0; i < getTableSize(string Rank_Table)){

			getInLinks(url,links_Vector);
			for(int j = 0; j < links_Vector.size(); j++)
			{
				pr += getPR(links_Vector[j]);
			}
			pr = 1 - DAMPENING_FACTOR + DAMPENING_FACTOR * pr;
			updatePR(url,pr);
			url = getNext();
		}

	}
	return true;
}