const fs = require('fs');
const file = process.argv[2];

function checkExistance(file){
  fs.access(file, fs.constants.F_OK, function(err) {
            if (!err) {
                fs.stat(file, function (error, stats){
                    if (!error) {
                        if (stats.isFile()){
                            fs.readFile(file, 'utf8', function (error, data) {
                                response.write("File:\n" + data);
                                response.end();
                        }}

                        else{
                            response.write("Directory");
                            response.end();
                          }}
                    }

                  }
            else {
                response.write("Not found");
                response.end();
              }
            }
}

checkExistance(file);

fs.access(file, fs.constants.F_OK, function(err) {
    if (!err) {
      fs.stat(file, function (error, stats){
          if (!error) {
            if (stats.isFile()){
              fs.readFile(file, 'utf8', function (error, data) {
                response.write("File:\n" + data);
                response.end();
              });
            }
            else{
              response.write("Directory");
              response.end();
            }
          }

      });
    }
    else {
        response.write("Not found");
        response.end();
      }
});
