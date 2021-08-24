class MeshdimnsionLoader:

    def getOptimalMesh(self, dictionary, columnRowRatio):
        for key in dictionary:
            if (columnRowRatio > dictionary[key][0]):
                continue
            else:
                optimalMesh = dictionary[key][1]
                break
        print(dictionary[key][2])
        print(" ***************************** ")
        return optimalMesh
   
    def getColumn15Dict(self):
        column15Dict = {
			1: [15/15, [15,15],"optimal mesh dimension is [15 x 15]"],
            2: [15/14, [15,14],"optimal mesh dimension is [15 x 14]"],
            3: [15/12, [15,12],"optimal mesh dimension is [15 x 12]"],
            4: [15/10,[15,10],"optimal mesh dimension is [15 x 10]"],
            5: [15/9,[15,9],"optimal mesh dimension is [15 x 9]"], 
            6: [15/8,[15,8],"optimal mesh dimension is [15 x 8]"],
            7: [15/6,[15,6],"optimal mesh dimension is [15 x 6]"],
            8: [15/5,[15,5],"optimal mesh dimension is [15 x 5]"]
            }
        return column15Dict

    def getColumn20Dict(self):
        column20Dict = {
            1: [20/20, [20,20],"optimal mesh dimension is [20 x 20]"],
            2: [20/18, [20,18],"optimal mesh dimension is [20 x 18]"],
            3: [20/16, [20,16],"optimal mesh dimension is [20 x 16]"],
            4: [20/15, [20,15],"optimal mesh dimension is [20 x 15]"],
            5: [20/14,[20,14],"optimal mesh dimension is [20 x 14]"], 
            6: [20/12,[20,12],"optimal mesh dimension is [20 x 12]"],
            7: [20/10,[20,10],"optimal mesh dimension is [20 x 10]"],
            8: [20/9,[20,9],"optimal mesh dimension is [20 x 9]"],
            9: [20/8,[20,8],"optimal mesh dimension is [20 x 8]"]
        }
        return column20Dict

    def getColumn25Dict(self):
        column25Dict = {
            1: [25/25, [25,25],"optimal mesh dimension is [25 x 25]"],
            2: [25/22, [25,22],"optimal mesh dimension is [25 x 22]"],
            3: [25/20, [25,20],"optimal mesh dimension is [25 x 20]"],
            4: [25/18, [25,18],"optimal mesh dimension is [25 x 18]"],
            5: [25/16,[25,16],"optimal mesh dimension is [25 x 16]"], 
            6: [25/15,[25,15],"optimal mesh dimension is [25 x 15]"],
            7: [25/14,[25,14],"optimal mesh dimension is [25 x 14]"],
            8: [25/12,[25,12],"optimal mesh dimension is [25 x 12]"],
            9: [25/10,[25,10],"optimal mesh dimension is [25 x 10]"]
            }        
        return column25Dict

    def getRow15Dict(self): 
        rowDict = {
			1: [5/15, [5,15],"optimal mesh dimension is [5 x 15]"],
            2: [6/15, [6,15],"optimal mesh dimension is [6 x 15]"],
            3: [8/15, [15,15],"optimal mesh dimension is [15 x 15]"],
            4: [9/15,[9,15],"optimal mesh dimension is [9 x 15]"],
            5: [10/15,[10,15],"optimal mesh dimension is [10 x 15]"], 
            6: [12/8,[12,15],"optimal mesh dimension is [12 x 15]"],
            7: [14/15,[14,15],"optimal mesh dimension is [14 x 15]"],
            8: [15/5,[15,15],"optimal mesh dimension is [15 x 15]"]
        }
        return rowDict

    def getRow20Dict(self):
        rowDict = {
            1: [8/20, [8,20],"optimal mesh dimension is [8 x 20]"],
            2: [9/20, [9,20],"optimal mesh dimension is [9 x 20]"],
            3: [10/20, [10,20],"optimal mesh dimension is [10 x 20]"],
            4: [12/20, [12,20],"optimal mesh dimension is [12 x 20]"],
            5: [14/20, [14,20],"optimal mesh dimension is [14 x 20]"],
            6: [15/20,[15,20],"optimal mesh dimension is [15 x 20]"], 
            7: [16/20,[16,20],"optimal mesh dimension is [16 x 20]"],
            8: [18/20,[18,20],"optimal mesh dimension is [18 x 20]"],
            8: [20/20,[20,20],"optimal mesh dimension is [20 x 20]"],
        }
        return rowDict

    def getRow25Dict(self):
        rowDict = {
            1: [10/25, [10,25],"optimal mesh dimension is [10 x 25]"],
            2: [12/25, [12,25],"optimal mesh dimension is [12 x 25]"],
            3: [14/25, [14,25],"optimal mesh dimension is [14 x 25]"],
            4: [15/25, [15,25],"optimal mesh dimension is [15 x 25]"],
            5: [16/25,[16,25],"optimal mesh dimension is [16 x 25]"], 
            6: [18/25,[18,25],"optimal mesh dimension is [18 x 25]"],
            7: [20/25,[20,25],"optimal mesh dimension is [20 x 25]"],
            8: [22/25,[22,25],"optimal mesh dimension is [22 x 25]"],
            9: [25/25,[25,25],"optimal mesh dimension is [25 x 25]"]
            }        
        return rowDict
       