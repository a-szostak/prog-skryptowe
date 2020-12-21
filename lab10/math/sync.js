const fs = require('fs');
const file = process.argv[2];

function checkExistance(file){
    try{
        fs.accessSync(file);
        if (fs.statSync(file).isFile()){
            return("File:\n" + fs.readFileSync(file, 'utf-8'));
        }
        else{
            return("Directory");
        }
        
    }
    catch (err){
        return "Not found";
    }
    
}



//console.log(checkExistance(file));

module.exports = checkExistance;