
MyDBsetup;
myPrefix = 'DH_';
infoFunc = @util_UpdateInfo;

%DELETE_TABLE_TRIGGER = true;

for SCALE = 13:14
for SEED = 20160331
for NUMTAB = 1:1

tname = [myPrefix 'pg' num2str(SCALE,'%02d') '_' num2str(SEED)];
TNadjUU = [tname '_TgraphAdjUU'];
TNadjUUDeg = [tname '_TgraphAdjUUDeg'];
TNadjJaccard = [tname '_TgraphAdjJaccard'];
TNadjJaccardD4M = [tname '_TgraphAdjJaccardD4M'];

alg02_Jaccard01_Graphulo;
pause(2);
alg02_Jaccard02_D4M;

TadjJaccard = DB(TNadjJaccard); TadjJaccardD4M = DB(TNadjJaccardD4M);

% Verification runs out of Java heap memory at SCALE 12 and larger
if SCALE < 12
    alg02_Jaccard03_Verify;
end

end
end
end