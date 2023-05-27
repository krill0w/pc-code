using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class healthPauseHide : MonoBehaviour
{
    [SerializeField] private bool isPaused;

    // Update is called once per frame
    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            isPaused = !isPaused;
        }

        if (isPaused)
        {
            ActiveateMenu();
        }

        else
        {
            DeactivateMenu();
        }
    }

    void ActiveateMenu()
    {
        transform.localScale = new Vector3(0, 0, 0);
    }

    public void DeactivateMenu()
    {
        transform.localScale = new Vector3(1, 1, 1);
    }
}