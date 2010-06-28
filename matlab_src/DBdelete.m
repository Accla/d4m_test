
function DBdelete(host,table)
% Delete Database Tables
%
% Returns nothing.
%
% Example:

%
% host='host_name'
% table='table_name'
% DBdelete(host,table)
%
%
%
% For help on creating database tables;
% type help DBcreate


ops = DBaddJavaOps('ll.mit.edu.d4m.db.cloud.D4mDbTableOperations',host);
ops.deleteTable(table);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% D4M: Dynamic Distributed Dimensional Data Model
% Architect: Dr. Jeremy Kepner (kepner@ll.mit.edu)
% Software Engineer: Mr. William Smith (william.smith@ll.mit.edu),
%  Mr. Charles Yee (yee@ll.mit.edu), Dr. Jeremy Kepner (kepner@ll.mit.edu)
% MIT Lincoln Laboratory
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% (c) <2010> Massachusetts Institute of Technology
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

