function T = putTriple(T,r,c,v);
%PUT inserts triples and its transpose into DB table.

  % Set chunk size in chars.
%  chunkBytes = 20e5;  % 10.5
  chunkBytes = 10e5;  % 8.9
%  chunkBytes = 5e5;  % 8.5

  % Get number of bytes.
  rByte = numel(r);   cByte = numel(r);   vByte = numel(v);
  ir = [0 find(r == r(end))];
  ic = [0 find(c == c(end))];
  iv = [0 find(v == v(end))];
  Nr = numel(ir)-1; 

  avgBytePerTriple = (rByte + cByte + vByte)/Nr;
  chunkSize = min(max(1,round(chunkBytes/avgBytePerTriple)),Nr);

  DB = struct(T.DB);

  for i=1:chunkSize:Nr
    i1 = min(i + chunkSize,Nr+1);
    rr = r((ir(i)+1):ir(i1));
    cc = c((ic(i)+1):ic(i1));
    vv = v((iv(i)+1):iv(i1));
    DBinsert(DB.instanceName, DB.host, T.name1, DB.user, DB.pass, rr, cc, vv, T.columnfamily, T.security );
    DBinsert(DB.instanceName, DB.host, T.name2, DB.user, DB.pass, cc, rr, vv, T.columnfamily, T.security );    % Insert transpose.
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

