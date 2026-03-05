# [ processing.py ] #

# ======== Setup ======== #

# [ Libraries ] #
import time

# [ Modules ] #
from .checks        import rate_password
from .utils         import DebugMsg
from ..data.save    import save_result
from .generator     import generate_password
from ..io.reader    import read_txt, read_jsonl, read_file # read_file unused


# ======== Main ======== #

def process_check( args, stats: dict=None ):
    """Processes arguments from group 'check'."""

    if args.password:
        _handle_single(args.password, args, stats)
    
    elif args.file:
        DebugMsg("warn", "Saving results, please wait...", True, True)

        weak_c = moderate_c = strong_c = 0
        
        for pwd in read_txt(args.file):
            i = 0
            
            result = rate_password(pwd, args.check_mode, verbose=False, user_stats=stats, cm_bypass=True)
            strength =  result[1]
            score =     result[2]

            if strength == "Weak":
                weak_c += 1

            elif strength == "Moderate":
                moderate_c += 1

            else:
                strong_c += 1
            
            save_result(pwd, args.check_mode, score, strength, time.strftime("%Y-%m-%d"))
            i += 1
            
        
        DebugMsg("load-ok", "Results successfully saved.", False, True)
        
        print("\n < ===== RESULTS ===== >")
        print(f" There is/are ({weak_c}) weak password(s).")
        print(f" There is/are ({moderate_c}) moderate password(s).")
        print(f" There is/are ({strong_c}) strong password(s).")
        
        DebugMsg("info", "Check results for more info.", True, True)


def process_generate( args, stats: dict=None ):
    """Processes arguments from group 'generate'."""
  
    generated = generate_password(args.check_mode, user_stats=stats, amount=args.count)
    results = []
    for p in generated:
        results.append(
            rate_password(p, args.check_mode, verbose=False, user_stats=stats, cm_bypass=True, isGenerator=True)
        )
    
    if args.count <= 5:
        _handle_single(p, args, stats=stats, isGenerator=True, generated=generated)
        
        return
    
    # save results if amount to generate too large
    DebugMsg("warn", "Number of passwords is larger. Saving results...", True, True)
    
    for i, p in enumerate(generated):
        save_result(p, args.check_mode, results[i][2], results[i][1], time.strftime("%Y-%m-%d"))

    DebugMsg("load-ok", "Generated passwords successfully saved.", False, True)



def _handle_single( password: str, args, stats: dict=None, isGenerator: bool=False, generated: list[str]=None ):
    """Handle saving single password."""

    _generated = generated if isGenerator and generated is not None else password

    result = rate_password(password, args.check_mode, verbose=False, user_stats=stats, cm_bypass=True)
    score = result[2]
    strength = result[1]
    
    #clean_strength = strip_ansi(strip_ansi)

    if args.output:
        DebugMsg("warn", "Saving results, please wait...", True, True)
        
        save_result(args.password, args.check_mode, score, strength, args.output)
        
        DebugMsg("load-ok", "Results successfully saved.", False, True)
    
    if not isGenerator:
        #print(f"{password} -> {score}")
        print(f" The password is {strength}.\n")
        print(f" * Check mode: {args.check_mode}")
        print(f" * Score: {score}")
        return
    
    for i, p in enumerate(_generated):
        print(f"\n Password [{i+1}] -> {p}")

