## ML System Lifecycle
- Machine learning pipelines require machine learning centric tests at various levels
    - Traditional tests
    - ML-Specific tests
        - Data and model tests
    - Monitoring and skew tests
    - Data prediction and system monitoring

## Testing Concepts for ML Systems
### Testing Scope
- Development environment
    - Unit, integration and acceptance tests
    - Differential tests
    - Benchmark tests
    - Load tests
- Production environment
    - Shadow mode testing
    - Canary releases
    - Observability & monitoring
    - Logging & tracing
    - Alerting
    
    ![alt text](images\testing_phases.png "Title")

### Why test?
- Confidence
    - Have confidence in your system
- Prediction
    - Your system's future reliability
    - Analyse the uncertainty incurred by any system change
- What change are we tracking?
    - Confidence that functionality remains unchanged

**Testing is the way we show our system functionality is what we expect it to be, even as we make changes to the system**

The real value of testing occurs with system change

### Testing ML Systems
- ML system = data + model + code
- Behaviour of ML systems is often learnt from data, as opposed to specified from code
- ML systems require extensive testing because the rules governing the system behaviour are less clearly defined

    ![alt text](images\key_testing_principles.png "Title")

### Testing theory
- Traditional tests
    - Unit tests 
        - Run on classes and functions
    - Integration tests
        - Run on an assembled components
    - System tests
        - End-to-end functionality of our system
- Tests are like armour
    - No armour, very vulnerable
    - Too much armour, cannot move

###