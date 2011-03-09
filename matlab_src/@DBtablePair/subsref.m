function A = subsref(T, s)
%SUBSREF Get entries from DB table pair.

  row = s.subs{1};
  col = s.subs{2};

  DB = struct(T.DB);

  if ( (numel(col) == 1) && (col == ':') )
    [retRows,retCols,retVals]=DBsubsrefFind(DB.instanceName,DB.host,T.name1,DB.user,DB.pass,row,col, T.columnfamily,T.security);
    A = Assoc(char(retRows),char(retCols),char(retVals));
  else
    [retRows,retCols,retVals]=DBsubsrefFind(DB.instanceName,DB.host,T.name2,DB.user,DB.pass,col,row, T.columnfamily,T.security);
    A = Assoc(char(retCols),char(retRows),char(retVals));
  end

end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% D4M: Dynamic Distributed Dimensional Data Model
% Architect: Dr. Jeremy Kepner (kepner@ll.mit.edu)
% Software Engineer: Dr. Jeremy Kepner (kepner@ll.mit.edu)
% MIT Lincoln Laboratory
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% (c) <2010> Massachusetts Institute of Technology
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

