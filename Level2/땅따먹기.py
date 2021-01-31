def solution(land):
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    return max(land[len(land)-1])

# #include <iostream>
# #include <vector>
# using namespace std;
#
# int maxGround(vector<int>& v, int idx){
#     int temp = 0;
#     for(int i = 0; i < 4; i++)
#         if(i != idx)
#             temp = max(temp, v[i]);
#     return temp;
# }
#
# int solution(vector<vector<int> > land)
# {
#     int answer = 0;
#     int size = land.size();
#     for(int i = 1; i < size; i++){
#         for(int j = 0; j < 4; j++){
#             land[i][j] += maxGround(land[i - 1], j);
#             answer = max(answer, land[i][j]);
#         }
#     }
#
#     return answer;
# }