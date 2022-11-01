#!/bin/bash
#TODO add all new ones
mkdir joblists


#these 3 and the other 3 should be merged
bash mkX.sh QA/QAplotsNdata 0
bash mkX.sh QA/QAplotsNdata 1
bash mkX.sh QA/QAplotsNdata 2

bash mkX.sh QA/dat2gif 0
bash mkX.sh QA/dat2gif 1
bash mkX.sh QA/dat2gif 2
bash mkX.sh QA/dat2gif 3

bash mkX.sh QA/PDFs 


bash mkX.sh QA/phaseDiagram 

bash mkX.sh QA/phaseCell

bash mkX.sh QA/coldGasFraction

bash mkX.sh QA/TvtCell 0
bash mkX.sh QA/TvtCell 1

bash mkX.sh QA/v_rms 0

bash mkX.sh QA/mixingMetric

bash mkXserial.sh QA/initRhoPhase

bash mkXserial.sh QA/TvtOrho 0
bash mkXserial.sh QA/TvtOrho 1
