% Test row and column search

AssocSetup3

DBsetup

tablename='SearchRowAndCol2TEST';
T = DB(tablename);
deleteForce(T);
T = DB(tablename);
% Insert some data
    put(T,A);


family='';
authorizations='';
db=struct(DB);
query=DBaddJavaOps('edu.mit.ll.d4m.db.cloud.D4mDbQuery', db.instanceName, db.host, tablename, db.user, db.pass);

query.setStartRowInclusive(java.lang.Boolean.TRUE.booleanValue);
query.setEndRowInclusive(java.lang.Boolean.TRUE.booleanValue);
query.setPositiveInfinity(false);
query.setDoAllRanges(false);
query.clearBuffers();

%%%%%%%%%%%%%%%%%%%%%%%%
%  Test T('a,:,b,', 'a,:,b,');
rowkey5='b,:,pat,'
colqual5='a,:,pa,'

T5 = T(rowkey5, colqual5)

rowResults = Row(T5);
index = findstr(rowResults,'pat');
checkIndex = isempty(index);
assert(checkIndex == 0,['No result - pat - found.']); 

index = findstr(rowResults,'car');
checkIndex = isempty(index);
assert(checkIndex == 0,['No result - car - found.']); 

%query.searchByRowAndColumn(rowkey5,colqual5,family,authorizations);
%query.doMatlabQuery(rowkey5,colqual5,family,authorizations);
%  rowString = query.getRowReturnString;
%  colString = query.getColumnReturnString;
%  valueString = query.getValueReturnString;
%display('******************************** ');
%display(['5.row= ' char(rowString)]);
%display(['5.col= ' char(colString)]);
%display(['5.val= ' char(valueString)]);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% D4M: Dynamic Distributed Dimensional Data Model
% Architect: Dr. Jeremy Kepner (kepner@ll.mit.edu)
% Software Engineer: Dr. Jeremy Kepner (kepner@ll.mit.edu)
% MIT Lincoln Laboratory
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% (c) <2010> Massachusetts Institute of Technology
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


