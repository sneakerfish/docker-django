import re
from election.models import Office, StateOffice, Party, State

def load_office(file):
    with open(file) as fp:
        for line in fp:
            line = line.rstrip()
            result = re.match(r"\s*(\d+)\.\s+(.*)", line)
            if result:
                o = Office.objects.create(code=result.group(1),
                                          name=result.group(2))


def load_state_office(file):
    # state offices look like this:
    #    006. Public Service Commissioner
    with open(file) as fp:
        for line in fp:
            line = line.rstrip()
            result = re.mach(r"\s*(\d+)\.\s+(.*)", line)
            if result:
                so = StateOffice.objects.create(code=result.group(1),
                                                name=result.group(2))

def load_party(file):
    # Parties look like this:
    #              0111  ANTI-BRODERICK DEMOCRAT
    with open(file) as fp:
        for line in fp:
            line = line.rstrip()
            result = re.match(r"\s*(\d+)\s+(.*)", line)
            if result:
                p = Party.objects.create(code=result.group(1),
                                         name=result.group(2))

def load_state(file):
    # States are listed with their group first and there are blank lines in between.
    #  Like this:
    #               EXTERNAL STATES
    #
    #    81.  Alaska (1959)
    #    82.  Hawaii (1959)
    area = ""
    with open(file) as fp:
        for line in fp:
            line = line.rstrip()
            # is it a blank line?
            if line == "":
                continue
            # is it a state with a date?
            result = re.match(r"\s*(\d+)\.\s+(.*)\s\((\d+)\)", line)
            if result:
                st = State.objects.create(code=result.group(1),
                                          name=result.group(2),
                                          year=result.group(3),
                                          area=area)
            else:
                # is it a state without a date?
                result = re.match(r"\s*(\d+)\.\s+(.*)", line)
                if result:
                    st = State.objects.create(code=result.group(1),
                                              name=result.group(2),
                                              year=None,
                                              area=area)

                else:
                    # Otherwise, it is an area
                    area = line.strip()

def load_candidate(file):
    with open(file) as fp:
        for line in fp:
            cand_num = line[0:2]
            year = line[3:5]
            state_code = line[6:8]
            office_code = line[8:9]
            district_no = line[9:12]
            asterisk = line[12:13]
            candidate_vote = line[19:28]
            election_month = line[27:29]
            election_type = line[29:30]
            party_code = line[30:34]
            name = line[34:]