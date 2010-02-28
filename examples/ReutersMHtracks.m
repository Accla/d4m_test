% Computes Facets in Reuters Entity data.

% Read in entities.
%A=ReutersEntityRead;

% Parse into time stamp and add to A.
%A=ReutersEntityTimeStamp(A);


% Turn into a general function.
% Atrack = FindTracks('NE_PERSON/*,','NE_LOCATION/*,','NE_TIME/*,')
% function Atrack = FindTracks(colItem,colLoc,colTime);
%
% Also can create Multiple Hypothesis tracks.
% Returns array of associative arrays contain MH for each item.
% MHtrack = FindMHT( �
%



x = 'NE_PERSON/DAMON HILL,';
y = 'NE_PERSON/GARY WONG,';
disp(['x=' x]);

tic;
  % Find docs that have person
  DocIDwPer = Row(A(:,x));

  Ax = A(DocIDwPer,:);

  % Find docs that have person and location.
  DocIDwPerLoc = Row(Ax(DocIDwPer,'NE_LOCATION/*,'));

  % Find docs that have person, location and time.
  DocIDwPerLocTime = Row(Ax(DocIDwPerLoc,'NE_TIME/*,'));
findOverlapsTime = toc; disp(['findOverlapsTime = ' num2str(findOverlapsTime)]);

tic;
% Get sub arrays.
  Aper = Ax(DocIDwPerLocTime,'NE_PERSON/*,');

  Aloc = Ax(DocIDwPerLocTime,'NE_LOCATION/*,');
  [EntAloc DocAloc temp] = find(Aloc.');


  Atime = Ax(DocIDwPerLocTime,'NE_TIME/*,');
  [EntAtime DocAtime temp] = find(Atime.');

  DocAtimeMat = Str2mat(DocAtime);
  EntAtimeMat = Str2mat(EntAtime);
  LocTime = Mat2str(EntAtimeMat(StrSearch(DocAtime,DocAloc),:));
constructTracksTime = toc; disp(['constructTracksTime = ' num2str(constructTracksTime)]);

tic;
  AmhTrack = Assoc(LocTime,EntAloc,1,@sum);
assocConstruct = toc; disp(['assocConstruct = ' num2str(assocConstruct)]);

spy(AmhTrack.');
